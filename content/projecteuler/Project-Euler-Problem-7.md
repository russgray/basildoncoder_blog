Title: Project Euler Problem 7
Date: 2008-10-26 21:58
Author: Russell Gray
Slug: Project-Euler-Problem-7

***[Problem 7](http://projecteuler.net/index.php?section=problems&id=7)***

> By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
> see that the 6th prime is 13.
>
> What is the 10001st prime number?

Ah, what a nice, straightforward, unambiguous spec! If only business software
specifications were so precise.

[Way back in problem 3]({filename}/projecteuler/Project-Euler-Problem-3.md), I took a bit
of a wander off-topic and built a prime generator in .Net using the [Sieve of
Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_eratosthenes). Armed with
this, problem 7 should be easy, right? The sieve implementation generates an
IEnumerable<long>, which is non-indexable (i.e. I can't just say
Primes()[10001]), but I can take the first 10,001 and then ask for the last
element, which will be the answer to the problem.

There's a problem with this, however. The sieve requires an upper bound during
initialisation. This means it's great for solving problems like "generate all
the primes less than 10,001", but not so great at answering questions like
"what is the 10,001st prime number?", since it requires foreknowledge of the
upper bound.

To illustrate the problem, I'll take a wild guess at the upper bound.
I'm going to guess that the 10,001st prime number is less than 99,999.
What happens?

    :::csharp
    var sieve = new SieveOfEratosthenes(99999);
    var result = sieve.Primes().Take(10001).Last();

This generates an answer of 99,991. If I enter this into the Project Euler
website, however, it tells me the answer is wrong. Gah! What went wrong? A
simple test reveals the problem:

    :::csharp
    var sieve = new SieveOfEratosthenes(99999);
    var primes = sieve.Primes().Take(10001);
    var count = primes.Count();

There's only 9,592 primes generated! As the [docs for
Take()](http://msdn.microsoft.com/en-us/library/bb503062.aspx) state (emphasis
mine):

> Take<TSource> enumerates source and yields elements until count elements have been yielded or source contains no more elements.

Damn. So, looks like my 99,999 guess was too small - with that as an upper
bound, the sieve only finds 9,592 primes, and I need the 10,001st. OK, I'll
bump it up by an order of magnitude:

    :::csharp
    var sieve = new SieveOfEratosthenes(999999);
    var result = sieve.Primes().Take(10001).Last();

This gives me the correct answer. Not exactly a wonderful solution though; the
idea of having to guess the upper bound is pretty horrendous, and if this was
real code it wouldn't be particularly maintainable - what if the requirements
changed and we had to find the *n*th prime, which happened to be >99,999? We'd
have to guess again. Ugh.

Worse, the sieve algorithm precomputes all the primes up to the specified
upper bound, meaning that in the above approach I've asked the sieve to
generate primes up to 999,999 (all 78,498 of them!) despite only needing
10,001. Not very efficient.

Fortunately, the upper bound can be calculated separately. [Where n > 8601, as
in this case, we can use the following
equation](http://primes.utm.edu/howmany.shtml):

$$p(n) < n (log_e n + log_e \cdot log_e \cdot n - 0.9427)$$

where p(*n*) is the *n*th prime number.

Alternatively, for flexibility in handling *n*<8601, we can use the less
accurate

$$(n) < n \cdot log_e \cdot log_e \cdot n$$

[which works for
*n*5](http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number).
We can easily precompute the answers for *n*<=5, or simply calculate on
demand.

The formula can be implemented on the sieve class, with a factory method
to help when we want to use it:

    :::csharp
    public static SieveOfEratosthenes CreateSieveWithAtLeastNPrimes(int n)
    {
        return new SieveOfEratosthenes((long)
                Math.Ceiling(UpperBoundEstimate(n)));
    }

    private static double UpperBoundEstimate(int n)
    {
        return n * Ln(n) + n * (Ln(Ln(n)));
    }

    private static double Ln(double n)
    {
        return Math.Log(n, Math.E);
    }

This leaves us with an overall solution like so:

    :::csharp
    var sieve = SieveOfEratosthenes.CreateSieveWithAtLeastNPrimes(10001);
    var result = sieve.Primes().Take(10001).Last();

This generates a total 10,018 primes, cutting the wasted effort from almost
70,000 superfluous primes to just 17, and takes around 20ms to execute on my
machine. Plenty fast enough, I think.
