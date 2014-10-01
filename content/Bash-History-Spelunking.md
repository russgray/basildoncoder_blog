Title: Bash History Spelunking
Date: 2008-04-14 14:50
Author: Russell Gray
Slug: Bash-History-Spelunking

Learned from Weiqi, who learned from [KageSenshi][1], about a [Fedora
Planet][2] shell history meme - post the results of running the following
command on your linux box:

    :::bash
    history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}' | sort -rn | head

I won't bother repeating the inevitable warning about the dangers of executing
random shell scripts you find on the Internet, because I'm lazy and mean.
Anyway, here's the results from my webhosting box:

    :::bash
    231 ll
    171 vim
    132 cd
    50 screen
    43 cat
    39 tail
    34 ls
    34 cls
    32 exit
    31 wget

'll' is an alias for 'ls -l', and 'cls' an alias for 'clear'. No real
surprises otherwise - I use vim for development over ssh, I tail my logs
occasionally, and live in GNU Screen.

Here's the output from my home box:

    :::bash
    254 ll
    181 cd
    148 sudo
    123 rm
    123 ffmpeg
    86 screen
    83 ls
    75 cls
    72 vim
    60 find

Quite similar actually, guess I'm set in my ways. The ffmpeg count is a bit of
an anomaly, since I used it a lot recently to re-encode a bunch of
[Futurama][3] rips for my mobile.

Not sure what to do with this remarkable intel, however. Perhaps I'll use the
data to generate an [Identicon][4] and use it as a favicon? Or, perhaps not.


[1]: http://blog.kagesenshi.org/2008/04/me-me.html
[2]: http://planet.fedoraproject.org/
[3]: http://en.wikipedia.org/wiki/Futurama
[4]: http://www.docuverse.com/blog/donpark/2007/01/19/identicon-explained