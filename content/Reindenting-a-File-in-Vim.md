Title: Reindenting a File in Vim
Date: 2007-12-07 18:19
Author: Russell Gray
Slug: Reindenting-a-File-in-Vim
Tags: vim, software engineering

I'm going to post a series of helpful Vim snippets here, particularly for
features that I don't necessarily use every day and hence forget about after a
while. By posting them here, I've got a nice easy one-stop-shop for finding
them.

The first tip is reindenting source code. Hitting `=` will reindent visually-
selected code , or you can also use a motion to constrain the affected area.
`gg=G` will reindent the entire file:

    :::csharp
    using System;
    namespace IndentExample
    {
    public class Indent
    {
    public static void Main(string[] args)
    {
    Console.WriteLine("badgerbadgerbadger");
    }
    }
    }

to

    :::csharp
    using System;
    namespace IndentExample
    {
        public class Indent
        {
            public static void Main(string[] args)
            {
                Console.WriteLine("badgerbadgerbadger");
            }
        }
    }

More info:
[http://www.vim.org/tips/tip.php?tip\_id=83](http://www.vim.org/tips/tip.php?tip_id=83)
