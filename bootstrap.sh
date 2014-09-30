#!/usr/bin/env bash

# install core packages
apt-get update
apt-get install -y vim-nox python python-dev python-virtualenv build-essential git libxml2-dev libxslt1-dev screen curl pandoc

# grab rc files for niceness
curl -s https://gist.githubusercontent.com/alexras/1144546/raw/fda3a9788eec53592fcb14bcfb6e00558436e322/.screenrc -o /home/vagrant/.screenrc
if [ ! -d /home/vagrant/.vim/bundle ]; then
    git clone https://github.com/gmarik/Vundle.vim.git /home/vagrant/.vim/bundle/Vundle.vim
fi
curl -s https://dl.dropboxusercontent.com/u/490360/vim/.vimrc -o /home/vagrant/.vimrc

# get plugins
if [ -d /opt/pelican-plugins ]; then
	rm -rf /opt/pelican-plugins
fi
git clone https://github.com/getpelican/pelican-plugins.git /opt/pelican-plugins

# do work in app directory
pushd /vagrant

if [ -d env ]; then
    rm -rf env
fi
virtualenv env

env/bin/pip install -r requirements.txt
env/bin/pip install git+git://github.com/bstpierre/pelican-comments#egg=pelican_comments
curl -s https://raw.githubusercontent.com/hutchison/markdown.subscript/master/subscript.py -o env/lib/python2.7/site-packages/markdown/extensions/subscript.py

popd
