Title: Ubuntu, Xmonad, and an Ode to Apt
Date: 2008-08-10 23:34
Author: Russell Gray
Slug: ubuntu-xmonad-and-ode-to-apt

This weekend I finally got around to updating my main Linux box from Ubuntu
7.10 to 8.04 (yes, I know, 4 months late - but moving fast!). The highly
excellent [xmonad][1] has made it into the main Ubuntu repositories, so I
discarded my own build and grabbed the packaged version - which promptly
didn't work as expected on my dual-head setup. Gah.

[A bit of googling suggested][2] that the problem lay with the upstream debian
package, which contained a build of libghc6-x11-dev that was compiled without
xinerama support. This left me with a choice of either waiting for the package
to get sorted out, or to do the build myself again. I decided to do my own
build rather than live without xmonad, but rather than mucking about with
tarballs I could at least now get the source from the package repository.

The appropriate steps, for anyone interested or having the same problem,
are:

1. Make sure libxinerama-dev is installed

2. Recompile libghc6-x11-dev and install it

3. Recompile libghc6-xmonad-dev and libghc-xmonad-contrib-dev against the new X11 lib

The apt-get incantations are:

    :::bash
    sudo apt-get install libxinerama-dev
    cd /tmp
    sudo apt-get source --compile libghc6-x11-dev
    sudo dpkg -i libghc6-x11-dev_1.4.1-1_i386.deb
    sudo apt-get build-dep libghc6-xmonad-dev
    sudo apt-get source --compile libghc6-xmonad-dev
    sudo dpkg -i libghc6-xmonad-dev
    sudo apt-get build-dep libghc6-xmonad-contrib-dev
    sudo apt-get source --compile libghc6-xmonad-contrib-dev
    sudo dpkg -i libghc6-xmonad-contrib-dev_0.6-4_i386.deb

A quick alt-q restart, and all is well.

I only mention all this because it's so easy in this day and age to take
something like apt for granted, and every so often it's worth taking a moment
to appreciate just how spectacularly good it really is. Where I work,
deployments are an endless source of headaches and grief, yet the complexity
of those deployments absolutely pales against the task of updating literally
millions of systems, all slightly different to each other, thousands of times
a day. It's just a joy to be able to say to apt "hey, go get me everything I
need to build package x, then build package x, then install it for me. And get
it right first time!".

In most cases, it does just that. It's an astonishing piece of software.


[1]: http://xmonad.org/
[2]: https://bugs.launchpad.net/debian/+source/haskell-x11/+bug/203594