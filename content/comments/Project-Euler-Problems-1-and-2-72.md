post_id: Project-Euler-Problems-1-and-2
Author: Hugh Redelmeier
Date: 2008-03-24 19:03:28
Author_Email: noreply@blogger.com
Author_IP: None

Problem 1 seems to be quite efficiently solved in the standard UNIX bc
program.  O(1) (ignoring the fact that bc uses arbitrary precision numbers).

    :::bash
    $ bc
    define s(n) { return n * (n + 1) / 2 }
    define t(n,m) { return s((n - (n % m)) / m) * m }
    t(999,3) + t(999,5) - t(999,15)
    233168
    quit

s(n) is the sum of the integers 1 to n, inclusive.
t(n,m) is the sum of all the integers that are multiples of m between 1 and n, inclusive.
The problem answer is the (sum of multiples of three) + (sum of multiples of
five) - (sum of multiples of 15 since they would have been counted twice).

Your C# program would choke if you changed 1000 to a googol.  The BC program says:

    23333333333333333333333333333333333333333333333333333
    33333333333333333333333333333333333333333333333166666
    66666666666666666666666666666666666666666666666666666
    66666666666666666666666666666666666666668

I haven't checked if that is correct. but it has about the right number of digits.
