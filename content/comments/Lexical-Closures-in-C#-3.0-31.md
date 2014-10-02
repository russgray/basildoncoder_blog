post_id: Lexical-Closures-in-CSharp-3_0
Author: Mark Giese
Date: 2013-06-11 14:18:57
Author_Email: noreply@blogger.com
Author_IP: None

Don't know where "funcs.ForEach" is coming from, but the following replacement
works.  The main point of the article is important and certainly not
invalidated by the typo.

    :::csharp
    foreach (Func f in funcs)
    {
        Console.WriteLine(f());
    }
