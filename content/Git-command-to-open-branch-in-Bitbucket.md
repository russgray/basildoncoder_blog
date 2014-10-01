Title: Git command to open branch in Bitbucket
Date: 2014-01-23 17:39
Author: Russell Gray
Slug: Git-command-to-open-branch-in-Bitbucket

George Brocklehurst has a [useful little script][1] for opening GitHub at a particular commit, right from the
command line. I've found this handy enough in the past that I've created an
equivalent for Bitbucket, which is what I use at work.

    :::bash
    #!/bin/bash

    bitbucket_remote=$(git remote -v | /c/Bin/grep -Eo 'bitbucket.org[:/][^.]+' | head -1)
    if [ -z $bitbucket_remote ]
    then
        echo "No bitbucket remote"
        exit
    fi

    bitbucket_url="https://${bitbucket_remote/://}/"
    if [ ! -z $1 ]
    then
        sha=$(git rev-parse $1)
        bitbucket_url="${bitbucket_url}commits/$sha"
    fi

    start $bitbucket_url

Installation instructions are the same as George's - name the script
git-bb and drop it on your PATH, then invoke it as a subcommand:

    :::bash
    $ git bb


[1]: http://georgebrock.com/blog/useful-git-aliases