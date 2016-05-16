from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer
import requests

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'blog/output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'russgray@188.226.200.128:22'
dest_path = '/apps/basildoncoder/blog'


def docker(cmd):
    local("docker run --rm -v /vagrant/blog:/blog russgray/blog-builder {}".format(cmd))

def drafts():
    # local("grep -ri '^Status:[[:space:]]*draft' content/**/*.md")
    docker("grep -ri '^Status:[[:space:]]*draft' content/")

def reflinks(f):
    local('formd -r < {0} | sponge {0}'.format(f))

def links():
    # local('linklint -quiet -no_anchors -doc linkdoc -root output -net /@ /drafts/@')
    docker("linklint -quiet -no_anchors -doc linkdoc -root /blog/output -net /@ /drafts/@")

def locallinks():
    # local('linklint -quiet -no_anchors -doc linkdoc -root output /@ /drafts/@')
    docker("linklint -quiet -no_anchors -doc linkdoc -root /blog/output /@ /drafts/@")

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}/*'.format(**env))

def build():
    docker('pelican -s pelicanconf.py content')
    locallinks()

def buildfullcheck():
    docker('pelican -s pelicanconf.py content')
    links()

def rebuild():
    clean()
    build()

def preview():
    clean()
    docker('pelican -s publishconf.py content')

@hosts(production)
def publish():
    preview()

    tmp_dir = '/home/russgray/apps/basildoncoder/blog'
    project.rsync_project(
        remote_dir=tmp_dir,
        exclude=".DS_Store",
        local_dir='blog/output/',
        extra_opts='-c',
    )
    sudo('rsync -rtv {}/ {}/'.format(tmp_dir, dest_path), user='www-data', shell=False)

@hosts(production)
def r_uname():
    run('uname -a')

