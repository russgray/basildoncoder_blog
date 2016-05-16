post_id: bash-history-spelunking
Author: Random Musings
Date: 2008-04-16 16:50:15
Author_Email: noreply@blogger.com
Author_IP: None

**Fedora Bash History Meme...**

I just learned about a Bash History Meme originated at Planet Fedora from a blog I read regularly.
In short, you run the following command in bash, and show your results.

    :::bash
    history | awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -...