post_id: The-PG-Wodehouse-Method-Of-Refactoring
Author: Dan
Date: 2008-03-24 01:19:44
Author_Email: noreply@blogger.com
Author_IP: None

... some of you guys talk about refactoring code "that's too far to the right" like the objective is to make your code look as cute as a button.

I tend to get the sneaking suspicion that these types don't understand that
code is run on a machine, in machine code form, and that this is what matters
to the successful operation of a program.

When I write a program to search for an entry in a four dimensional array with
two sparse dimensions, there will be alot of nesting in the text.  Wrapping it
in functions so you can un-nest it is *not* going to improve the algorithm,
it's just going to make it slower by introducing parameter stuffing into the
loop.

I tend to do almost all of my refactoring by:

1. removing lazy function calls (strlen() twice!?  regular expressions to find
0x20 space character!?  malloc() every 16-byte struct!?)

2. replacing recursion with iteration

3. hoisting code out of loops

4. removing as many cache and page misses as possible

5. refactoring branching to reduced or non-branching form and minimizing other
instruction pipe flushes.

I find that clean, well written code is self obviating and so rarely comment.
In C, even a scripting language written this way won't exceed 8000 lines.

In rare cases where an obscure trick is used to accomplish something
important, I use comments.  This happened twice for my scripting engine - for
the lexer switch's duff's device, and for the on-the-fly compiler's stack
handling.

Best Regards,
Dan
