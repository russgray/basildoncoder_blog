Title: Killing and Reviving an Aspire One
Date: 2009-02-08 21:01
Author: Russell Gray
Slug: Killing-and-Reviving-an-Aspire-One

I just spent 2 hours reviving my Aspire One netbook after inadvertently
killing it whilst fiddling about configuring
[dropbox](http://www.getdropbox.com). I found the whole process
unnecessarily fiddly and information on the interwebs to be a bit
scarcer than I would have liked, so I'm documenting it here in case I
need it in the future. Hopefully it'll be useful to someone else too.

So, the cause of death was a typo when trying to set up the dropboxd
daemon to start automatically on boot. I'm not running nautilus so
couldn't use one of the prepackaged releases, and it's completely my
fault that I made a mess of installing the vanilla x86 build.

After making the fatal change and rebooting, the system would only boot
up to a blank black screen with a default X mouse cursor. This is
because the system was trying to run my broken command, failing, and
therefore never getting to the main desktop.

In the world of normal linux, there's all sorts of ways of dealing with
this, but despite plenty of googling I couldn't find a way to use
run-level 2 or 3 on an Aspire One, and the Ctrl+Alt+F1-F6 key combos for
switching away from X to a terminal don't work either. There seems to be
no way of preventing the system following the same doomed process over
and again if you break X.

Frustrated, I thought about using the restore disk, but that's a nuclear
option - it re-paves the whole machine, so bye-bye data. That seemed a
bit drastic when all I needed to do was edit a single text file to fix
the system.

Ironically, this was happening as a result of me trying to install a
file sync system as a simple backup. Grr.

Still, like countless thousands before me, I was saved by a live linux
distro - in this case, a USB bootable one (since the Aspire One has no
optical drive). Following the
[instructions](http://www.pendrivelinux.com/feather-linux-on-usb/)^[1]^
at [pendrivelinux](http://www.pendrivelinux.com/) I created a bootable
Feather Linux USB drive, and booted the netbook from it by hitting F12
on the post screen and selecting to boot from the USB stick.

At the boot prompt, I used 'knoppix 3' to boot the system up to a
command line, mounted /dev/hdc1 as an ext2 filesystem, and fixed my
typo. Reboot, and tada! Everything was working again (well, after
hitting Fn-F7 to reenable the touchpad, which I had accidentally
disabled whilst mashing the keyboard in frustration at the sight of a
blank screen about an hour earlier, heh).

^[1]^ Note that I had to use a newer version of syslinux than the one
referenced on pendrivelinux. [This
one](http://www.kernel.org/pub/linux/utils/boot/syslinux/Old/syslinux-3.36.zip)worked
for me.
