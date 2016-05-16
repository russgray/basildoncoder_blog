post_id: lexical-closures-in-c-30
Author: mabra
Date: 2010-02-12 23:33:43
Author_Email: noreply@blogger.com
Author_IP: None

Hi !

I am just dealing with captured variables in creating Tasks and came onto the
same idea (using a local variable, copying the loop vars value).

Just don't work and return different results on each run!

BTW, I find lambda's too abstract and cannot understand them. So you also?

Your code:

    :::csharp
    funcs.ForEach(f => Console.WriteLine(f()));

does not compile ....
(No overload for method 'ForEach' takes '1' arguments)

br--mabra
