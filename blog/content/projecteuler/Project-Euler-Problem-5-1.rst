Project Euler Problem 5
#######################

:date: 2008-06-10 12:47
:author: Russell Gray
:slug: project-euler-problem-5-1
:status: draft

On to the next Project Euler problem (after a bit of a hiatus)...

`Problem 5`_
------------

    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest number that is *evenly divisible* by all of the
    numbers from 1 to 20?

In common with many of the other Euler problems, there's a brute-force
way to solve this, and a clean algorithmic way. And in common with my
other Euler posts so far, I'll start with the brute-force way ;-)

This problem can be tackled head-on with the following approach: Start
from *n*=1 and increment in a loop. Test each value of *n* by attempting
to divide it by all numbers *m* from 1 to 20. The first number to pass
the test (i.e. *n* mod *m* is 0 for all values of *m*) is the answer.

.. code-block:: c#

    private static long BruteForceSolver()
    {
        long result;
        for (result = 1; !Check(result); ++result)
                ;
        return result;
    }

    private static bool Check(long result)
    {
        for (int i = 1; i <= 20; ++i)
        {
            if (result % i != 0)
                return false;
        }
        return true;
    }

This works, but it takes >12 seconds to execute on my PC, so it's not
what you'd call efficient (though it is well within the Euler execution
time guidelines).

Some speed gains can be achieved by exploiting the information provided
in the question itself. We are told that 2520 is the lowest number
evenly divisible by all numbers from 1 to 10. Since the problem space (1
to 20) includes all these numbers, the answer must also be evenly
divisible by 2520. This allows much bigger increments each loop - rather
than incrementing by 1, why not increment by 2520? And since the answer
must be greater than or equal to 2520, why not start the loop there
instead of 1? Finally, since we already know that 1 to 10 divide evenly
into 2520, each inner loop only needs to check numbers 11 to 20.

That should speed things up a bit:

.. code-block:: c#

    private long BruteForceSolver()
    {
        long result;
        for (result = 2520; !Check(result); result += 2520)
            ;
        return result;
    }

    private bool Check(long result)
    {
        for (int i = 11; i <= 20; ++i)
        {
            if (result % i != 0)
            return false;
        }
        return true;
    }

And indeed, on my machine this is now down to 150ms or so. It's still
not a very nice way to tackle the problem, though.

Thinking about it from a different angle yields an altogether smarter
approach. Imagine we are looking for the lowest number evenly divisible
by the numbers 1 to 2.

.. math::

    [1, 2]

Well that's easy; since there are only two numbers we just find the
lowest common multiple (LCM), which in this case is 2 (since :math:`2
\bmod 2 = 0`, and :math:`2 \bmod 1 = 0`). If we call this sequence |s1|,
we can say that :math:`LCM(s_1)=2`.

OK, now imagine we are solving the same problem for |s2|, which contains
the numbers 1 to 3.

.. math::

    [1, 2, 3]

You'll notice that |s2| contains |s1| in its entirety. :math:`LCM(s_2)`
must therefore be a multiple of :math:`LCM(s_1)`, so we can rewrite |s2|
as :math:`[LCM(s_1), 3]`, or :math:`[2,3]`). Now we are down to two
numbers again, so we can calculate the LCM of 2 and 3, which is 6, so
:math:`LCM(s_2)=6`.

OK, now we solve the problem for the first 4 numbers (|s3|).

.. math::

    [1, 2, 3, 4]

This sequence contains |s2|, therefore :math:`LCM(s_3)` is a multiple of
:math:`LCM(s_2)`. We can rewrite |s3| as :math:`[LCM(s_2), 4]`, or
:math:`[6, 4]`. Thus, :math:`LCM(s_3)=12`.

This can be repeated as many times as necessary. Generally, we have
:math:`s_n = [LCM(s_{n-1}), n+1]` where :math:`n > 0`.

This looks recursive, but a better way to think of it is as an excellent
example of a fold. A fold is one of the fundamental tools of functional
programming. In fact, it is perhaps the most fundamental, since map,
filter etc can be implemented as right folds [1]_.

I won't inflict my pitiful Photoshop skills on anyone by trying to
graphically represent a fold - try looking at `this Wikipedia
article`_ if
you want to try and visualise it.

Broadly, the behaviour of a fold is to apply a combining function to
elements in a list (or other data structure) and accumulate the results.
That's exactly what we want here - our combining function is LCM, and
our accumulating value is the LCM of the whole list. Effectively, for
list |s3| above, we have

.. math::

    LCM(s_3)=LCM(LCM(LCM(1,2),3),4)=12

Note how the result of the innermost LCM (applied to values 1 and 2)
becomes a parameter to the next LCM, which in turn becomes a parameter
to the outermost LCM which returns the result we want.

By using a fold, we can generalise. In Haskell, the whole problem is a
one-liner:

.. code-block:: haskell

    foldl lcm 1 [1..20]

The 1 passed in as a parameter represents the terminating value to use
when the end of the list is reached. It is common for this value to be
the first element of the list, so Haskell provides a convenience
function that removes the need to specify it as a parameter:

.. code-block:: haskell

    foldl1 lcm [1..20]

Not all languages and platforms provide an LCM function right out of the
box, so to take this neat Haskell solution and port it to .Net, the LCM
function needs to be implemented. This is easily done in terms of the
greatest common divisor (GCD) like so:

.. math::

    LCM(a, b) = \frac{a\cdot b}{GCD(a, b)}

.Net doesn't provide a GCD function either, so I'll implement it using
`Euclid's Algorithm`_ as an extension method on long ints:

.. code-block:: c#

    public static long GCD(this long a, long b)
    {
        while (b != 0)
        {
            long tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

With GCD defined, LCM can be implemented as above:

.. code-block:: c#

    public static long LCM(this long a, long b)
    {
        return (a * b) / a.GCD(b);
    }

With this in place, it's a simple matter to use .Net's equivalent of
fold - a method on IEnumerable<T\> called Aggregate - to get the
answer [2]_:

.. code-block:: c#

    return LongEnumerable.Range(1, 20)
        .Aggregate(1L, (curr, next) => curr.LCM(next));

And indeed, the same basic pattern can be used to solve the problem in a
number of languages. In F#, given implementations of LCM and GCD as
above, we have:

.. code-block:: f#

    List.fold_left lcm 1 [1..20]

And in ruby:

.. code-block:: ruby

    require 'rational'
    (1..20).inject { |c, n| c.lcm n }

Given that the right algorithm makes this problem a fairly trivial
expression in all these languages, it's pretty hard to identify which is
the nicest. I think overall I'll give the nod to Haskell, however, for
not making me implement LCM and because I find ruby's 'inject' a less
intuitive function name than foldr (but that's probably because I
learned the technique in Haskell in the first place and am set in my
ways...)

.. _Problem 5: http://projecteuler.net/index.php?section=problems&id=5
.. _this Wikipedia article: http://en.wikipedia.org/wiki/Fold_(higher-order_function)
.. _`Euclid's Algorithm`: http://en.wikipedia.org/wiki/Euclidean_algorithm

.. [1] For example, in F#:

    .. code-block:: f#

        let filter p lst = List.fold_right (fun x xs -> if p x then x::xs else xs) lst []
        let map f lst = List.fold_right (fun x xs -> f x :: xs) lst []

.. [2] 
    Note that in this code LongEnumerable is just a very simple partial
    reimplementation of Enumerable, using longs instead of ints

.. |s1| replace:: s\ :sub:`1`\ 
.. |s2| replace:: s\ :sub:`2`\ 
.. |s3| replace:: s\ :sub:`3`\ 
.. |sn| replace:: s\ :sub:`n`\ 
