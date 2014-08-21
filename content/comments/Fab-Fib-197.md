post_id: Fab-Fib
Author: Trevor Bernard
Date: 2008-03-24 16:28:38
Author_Email: noreply@blogger.com
Author_IP: None

The Haskell implementation is just a little dynamic programming. It can easily but not quite as elegantly be done in any procedural language.<br /> <br />int fib[50];<br />fib[0] = 0;<br />fib[1] = 1;<br />for(int i=2; i<50; i++) {<br />    fib[i] = fib[i-2] + fib[i-1];<br />}
