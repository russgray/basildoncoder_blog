post_id: Bash-History-Spelunking
Author: Random Musings
Date: 2008-04-16 16:50:15
Author_Email: noreply@blogger.com
Author_IP: None

<strong>Fedora Bash History Meme...</strong><br /><br />I just learned about a Bash History Meme originated at Planet Fedora from a blog I read regularly.<br />In short, you run the following command in bash, and show your results.<br /><br />history | awk &#39;{a[$2]++ } END{for(i in a){print a[i] &quot; &quot; i}}&#39;|sort -...
