Title: Project Euler Problem 3
Date: 2008-04-07 13:38
Author: Russell Gray
Slug: Project-Euler-Problem-3

Next up in the list of Project Euler problems is this one:

<p>
***[Problem
3](http://projecteuler.net/index.php?section=problems&id=3)***  

> The prime factors of 13195 are 5, 7, 13 and 29.
>
> </p>
> What is the largest prime factor of the number 600851475143?

This, obviously, is a factorisation problem. There is a colossal amount
of material on the web for dealing with prime factorisation - a simple
[google search](http://www.google.co.uk/search?q=prime+factorization)
pulls up lots of information. Prime factorisation (and the difficulty of
doing it with sufficiently large numbers) is at the heart of the
cryptographic methods we currently use on the internet - every time you
buy something from Amazon, you are protected by the fact that evil
black-hats can't find the prime factors of your encryption key fast
enough to steal your credit card number (OK, bit of a generalisation,
but that's the gist).

One of the key phrases in the above paragraph is 'sufficiently large
numbers'. For a computer, 600851475143 is not a particularly big number,
so this problem can be brute-forced fairly easily. Of course, not all
brute force approaches are created equal. The most naive algorithm would
be something along the lines of a three-pass sweep - firstly test *every
single number* between 2 and 600851475143 to see if it divides cleanly
into 600851475143 (pass 1); then test each factor from pass 1 to see if
it is prime (pass 2); and finally take the biggest of the pass 2 numbers
to get your answer (pass 3).

This would work, but it sucks.

Fortunately, it's easy to optimise. Let the prime factors of our number
N be f~1~, f~2~ ... f~n~. If I start with the lowest prime number and
work up from there looking for a factor, I know that the first factor I
find will be prime (since if it wasn't prime, it would have factors of
its own, which by definition would also be factors of our target
number). This number is f~1~. I can divide the target number by f~1~ and
then factorise the result to find f~2~. Continuing this process will
result in a list of prime factors, and then it's simply a case of
selecting the largest.

<p>
I can optimise further by not resetting the factor to the lowest prime
number each time - since having found f~1~ I know that there aren't any
smaller factors, so I don't have to waste time looking for them. Here's
the implementation in python:

    def primeFactors(n, factor):    factors = [] while (n % factor != 0):        factor = factor + 1    factors.append(factor) if n > factor:        factors.extend(primeFactors(n / factor, factor)) return factorsprint max(primeFactors(600851475143, 2))

Note that in the recursive call the current factor is retained, so that
the code doesn't repeat itself.

This executes pretty quickly, but it could be better. For a start, since
600851475143 is odd there's no need to start with the only even prime
number (2). Instead, I could just start at 3, and in the while loop skip
over even numbers. This would cut the number of tested numbers in half.

A more efficient trial division approach, however, would be to generate
a list of primes, divide 600851475143 by each prime to find the prime
factors, then simply select the largest. To use this solution, a prime
number generator is needed.

This is an interesting diversion - I've peeked at some of the other
Project Euler problems and know that prime numbers will pop up again, so
it may prove useful to have a generator handy for when I get to those.
Some languages, like Ruby, have library functions that can give you
primes, but other languages don't. If you're not interested in
generating primes and just want to know the answer to problem 3, execute
the code above and you're free to get down from the table.

***A Random Walk Off-Topic***

The simplest way to generate primes is known as the [Sieve of
Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) after
the Greek mathematician who invented it. In principle it's
straightforward - take a list of all integers up to an arbitrary limit,
then starting from 2 (the smallest prime), mark all the numbers that are
multiples of 2. Then move to the next unmarked number (i.e. 3) and mark
all the multiples of 3. Then you move to the next unmarked number (5,
since 4 was marked as a multiple of 2) and mark all multiples. And so
on, until you get to the end of your list. Whatever numbers remain
unmarked are all the primes up to your arbitrary limit.

.Net lacks a built-in prime generator, so to demonstrate the algorithm
I'll create a simple C\# implementation. The list of numbers is
represented as an array of booleans, all set to true by default except
indexes 0 and 1 (since we aren't interested in evaluating those numbers
as prime).

The other requirement for a funky contemporary .Net implementation is,
of course, to expose the results with IEnumerable. This achieves two
things - firstly, it lets the sieve class control enumeration and thus
skip over the marked numbers (making the calling code cleaner), and
secondly it lets me use LINQ to query it.

<p>
So, here's the code:

    public class SieveOfEratosthenes{ private bool[] m_numbers; public SieveOfEratosthenes(long limit)    {        m_numbers = new bool[limit + 1]; for (long l = 2; l < m_numbers.LongLength; ++l)        {            m_numbers[l] = true;        } for (int i = 2; i != -1;                i = Array.FindIndex(m_numbers, i + 1,                    b => b == true))        { for (int j = i * 2; j < m_numbers.Length; j += i)                m_numbers[j] = false;        }    } public IEnumerable<long> Primes()    { for (long i = 2; i < m_numbers.LongLength; ++i) if (m_numbers[i]) yield return i;    }}

Fairly straightforward. Basically, I start by marking 2 as prime. Then,
an inner loop sets all multiples of 2 to false, since no (other) even
numbers are prime. Each time round the loop, we find the next true
element of the array (which will have a prime index), and mark all
multiples false as per the description above. The loop terminates when
FindIndex fails to find any more true elements.

This results in an array where the only elements with a value of true
are those with a prime index. This makes the actual IEnumerable
generator very easy to write - it yield returns the index whenever it
finds a true element.

There's a problem with this code, however, that makes it unusable with
Euler problem 3 (at least in .Net - hence why I called it a 'diversion'
earlier, rather than an alternative solution). In .Net, you can't create
an array with 600851475143 elements, since an array with 600851475143
elements is way above the maximum array size limit of 2GB. Even if each
element is only a single byte, 600851475143 bytes is about 560GB.

Therefore, you can't create a sieve big enough to solve the problem.

When using trial division it seems that it is enough to only generate
primes up to the square root of N, though there are cases when this is
not true (e.g. where N=15, sqrt(N) = \~3.873, but the largest prime
factor of 15 is 5), and I don't have the maths (yet!) to know how big a
fudge-factor is needed. I've seen a solution on the Project Euler forum
that generates primes up to sqrt(N) + 10, which solves the example of
N=15 above, but does it solve ALL cases? Another approach might be to
generate the list of primes such that the largest prime in the list is
the first prime \> sqrt(N) - but now I'm completely guessing.

<p>
Still, for numbers that fit inside the 2GB limit, we can find the
largest factor easily.

    var sieve = new SieveOfEratosthenes(15);

<p>
Now I have my IEnumerable sieve, I can craft a LINQ query to find the
largest factor. All I need to do is filter my list of primes for those
which divide directly into 15 and call the Max() method:

    return (from p in sieve.Primes() where 15 % p == 0 select p).Max();

Done! And I have a handy reusable prime generator for later on.
