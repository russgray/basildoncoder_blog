Title: Lexical Closures in C# 3.0
Date: 2008-07-01 17:49
Author: Russell Gray
Slug: Lexical-Closures-in-CSharp-3_0

There's a [slightly weird article][1] up on [Dobbs Code Talk][2] this week, speculating that aggregate
functions are "the next big programming language feature" after closures. The
slight weirdness comes from the fact that both features have been around for
decades, and not just in dusty academic languages either.

Still, there's some interesting discussion in the comments about whether
.Net's closures are proper first-class lexically-scoped closures. The
answer is yes - but with a fun twist.

The twist has been around for a long time - [Brad Abrams][3] blogged about it 
[way back in 2004][4], for
instance - but it's probably worth going over it again, since the recent
arrival of LINQ and lambda syntax in C# 3.0 will presumably lead to more
people being bitten by this as the use of closures becomes more mainstream.

A key thing to remember is that C# lambdas are just anonymous delegates
in skimpy syntax. Behind the scenes the compiler turns them into classes
- if you were looking at disassembled MSIL you wouldn't be able to tell
whether the code was written with lambda syntax or anonymous delegate
syntax. Therefore, the issue discussed by Brad has not gone anywhere.

Lets revisit the problem, with a 2008 sheen applied (i.e. I'll use
lambda syntax rather than anonymous delegate syntax). What does the
following code display?

    :::csharp
    Func<int>[] funcs = new Func<int>[10];
    for (int i = 0; i < 10; ++i)
    {
        funcs[i] = () => i * i;
    }
    funcs.ForEach(f => Console.WriteLine(f()));

If you answered something along the lines of "prints the square of every
number between 0 and 9" you'd be...wrong. Really, try it out. See?

Now, a lexical closure is supposed to capture its environment, meaning
that the lambda stored on the first loop would capture i when i==0, the
second loop would capture i when i==1, and so on. If this happened, then
executing all the lambdas would indeed result in the squares of the
numbers 0-9 being printed. So what gives?

The problem stems from the fact that the lambda is binding itself to a
variable that is accessible outside the closure, which is being changed
in every iteration of the loop. The closure doesn't capture the value of
i, it captures a reference to i itself, which is mutable.

You could actually make a case that this is bad code anyway, since it
gives two responsibilities to the loop index - control the loop, and act
as data in the closures. If we were being pedantic, we could split the
responsibilities by creating a new variable, j, to be the closure data
each iteration, and let i concentrate on being an index:

    :::csharp
    for (int i = 0; i < 10; ++i)
    {
        int j = i;
        funcs[i] = () => j * j;
    }

Lo and behold, the code now works! Pedantry rules! Take a look with
Reflector or ildasm to see what's going on here. The executive summary
is that the compiler captures the environment (i in the first example, j
in the second) by creating a member variable within the class it
generates for the closure. Previously, since the same instance of i
lived for the entire duration of the loop, only one instance of the
generated class was created and shared. Now, however, a new instance of
the generated class is created in each iteration of the loop (since j is
scoped within the loop body and thus we have a new j every time round).
Thus, the data is not shared and we get the expected output.

There are two important points to consider here:

1. The problem goes away if you write code more declaratively. Do away
with the clunky for loop and everything works OK.

        :::csharp
        Enumerable.Range(0, 10).Select(x => x * x);

2. It isn't always bad that multiple closures can capture a reference -
since one closure can 'see' updates made to the shared data by another
closure, you could use this as a coordination mechanism.

This is not an issue that's going to crop up every day - the example
above is fairly contrived - but knowing about it will save some painful
debugging sessions when inevitably you do run into it. The fix is always
to take a local copy of the mutable data to coerce the compiler into
generating code that creates multiple instances of the class generated
to represent the closure.

Simple, yes? ;-)


[1]: http://dobbscodetalk.com/index.php?show=The-next-big-programming-language-feature-after-closures.html
[2]: http://dobbscodetalk.com/
[3]: http://blogs.msdn.com/brada/default.aspx
[4]: http://blogs.msdn.com/brada/archive/2004/08/03/207164.aspx