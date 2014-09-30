Title: Fab Fib
Date: 2008-01-26 15:49
Author: Russell Gray
Slug: Fab-Fib
Tags: coding, software engineering

[Scott Hanselman](http://www.hanselman.com/blog/) continues his
[Weekly Source Code](http://www.hanselman.com/blog/CategoryView.aspx?category=Source+Code)
series with a look at algorithms for generating the
[Fibonacci sequence](http://en.wikipedia.org/wiki/Fibonacci_number) in a
[variety of different languages](http://www.hanselman.com/blog/TheWeeklySourceCode13FibonacciEdition.aspx).
He misses my favourite implementation, though fortunately a wise
commenter has already sought to correct such an egregious error. As is
so often the case, it is Haskell that provides the most elegant yet
mind-bending alternative:

    :::haskell
    fibonacci n = fib!!n
        where fib = 0 : 1 : zipWith (+) fib (tail fib)

This little beauty appends a list with its own tail *while it's still
being generated* and lazily sums the elements. On top of that, it's
*fast*, since unlike most naive recursive Fibonacci generators it
doesn't waste time recalculating previous values. In fact, it runs in
linear time, that is *O(n)*, and on a fairly modest 2GHz Athlon XP will
calculate the 50,000th Fibonacci number in around 600 milliseconds. By
contrast, the naive recursive implementation in C# (see below, adapted
and corrected from the code Scott posted) takes 28 seconds to calculate
the 45th number, on a much more powerful Core Duo machine.

    :::bash
    $ time ./Fibs.exe
    1134903170
    Execution time: 00:00:28.2930000

    real    0m28.382s
    user    0m0.000s
    sys     0m0.031s

As implemented, you can't go much higher than this since the 47th number
in the sequence (2971215073) is too big to store in a 32-bit signed int.
Asking for the 50,000th number results in an immediate stack overflow,
which is the runtime's way of saying "don't be ridiculous, mate".

Of course, the C# version could be made many times faster and more
efficient by implementing it iteratively (i.e. with a for loop), but
this is less natural since the Fibonacci sequence is a recurrence
relation and therefore best expressed recursively. The beauty of the
Haskell version is that it combines expressiveness with performance,
always a happy combination.

    :::csharp
    using System;

    namespace Fibs
    {
        class Program
        {
            static void Main(string[] args)
            {
                DateTime start = DateTime.Now;
                Console.WriteLine(Fibonacci(45));
                Console.WriteLine("Execution time: {0}",
                    DateTime.Now.Subtract(start));
            }

            static int Fibonacci(int n)
            {
                if (n == 0 || n == 1)
                    return n;
                return Fibonacci(n - 1) + Fibonacci(n - 2);
            }
        }
    }
