from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer
import requests

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'russgray@188.226.200.128:22'
dest_path = '/apps/basildoncoder/blog'

def drafts():
    local("grep -ri '^Status:[[:space:]]*draft' content/**/*.md")

def reflinks(f):
    local('formd -r < {0} | sponge {0}'.format(f))

def links():
    local('linklint -quiet -no_anchors -doc linkdoc -root output -net /@ /drafts/@')

def locallinks():
    local('linklint -quiet -no_anchors -doc linkdoc -root output /@ /drafts/@')

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}/*'.format(**env))

def build():
    local('env/bin/pelican -s pelicanconf.py content')
    locallinks()

def buildfullcheck():
    local('env/bin/pelican -s pelicanconf.py content')
    links()

def rebuild():
    clean()
    build()

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    clean()
    local('env/bin/pelican -s publishconf.py content')

@hosts(production)
def publish():
    preview()

    tmp_dir = '/home/russgray/apps/basildoncoder/blog'
    project.rsync_project(
        remote_dir=tmp_dir,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        extra_opts='-c',
    )
    sudo('rsync -rtv {}/ {}/'.format(tmp_dir, dest_path), user='www-data', shell=False)

@hosts(production)
def r_uname():
    run('uname -a')

