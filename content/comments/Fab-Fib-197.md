post_id: fab-fib
Author: Trevor Bernard
Date: 2008-03-24 16:28:38
Author_Email: noreply@blogger.com
Author_IP: None

The Haskell implementation is just a little dynamic programming. It can easily but not quite as elegantly be done in any procedural language.

    int fib[50];
    fib[0] = 0;
    fib[1] = 1;
    for (int i=2; i<50; i++) {
        fib[i] = fib[i-2] + fib[i-1];
    }
