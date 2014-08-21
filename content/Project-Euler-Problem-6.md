Title: Project Euler Problem 6
Date: 2008-08-14 01:00
Author: Russell Gray
Slug: Project-Euler-Problem-6

<div class="problem_content">
Onwards to...

</div>
<p>
***[Problem
6](http://projecteuler.net/index.php?section=problems&id=6)***  

> The sum of the squares of the first ten natural numbers is,
>
> <div style="text-align: center;">
> 1^2^ + 2^2^ + ... + 10^2^ = 385
>
> </div>
> The square of the sum of the first ten natural numbers is,
>
> <div style="text-align: center;">
> (1 + 2 + ... + 10)^2^ = 55^2^ = 3025
>
> </div>
> Hence the difference between the sum of the squares of the first ten
> natural numbers and the square of the sum is 3025 - 385 = 2640.
>
> Find the difference between the sum of the squares of the first one
> hundred natural numbers and the square of the sum.

<p>
Bit of a disappointment, problem 6; it's too easy. [It's rated as the
third-easiest](http://projecteuler.net/index.php?section=problems&sort=difficulty),
i.e. easier than problems
[3]({filename}/Project-Euler-Problem-3.md),
[4]({filename}/Project-Euler-Problem-4.md),
and
[5]({filename}/Project-Euler-Problem-5.md)
which I've already covered. In fact, for my money it's easier than
problem
[2]({filename}/Project-Euler-Problem-1-and-2.md)
as well. Ah well, the difficulty ramps up soon enough, trust me. Here's
the very simple python solution:

~~~~ {language="python" name="code"}
sum_sq = sum([ x*x for x in xrange(1, 101)])sq_sum = sum(xrange(1, 101)) ** 2print sq_sum - sum_sq
~~~~

As you can see, it's pretty intuitive. You sum the squares, square the
sum, and calculate the difference. The answer is basically in the
description, you just have to scale up a little.

<p>
There's not much else to say about this one. Even if I abandon the
functional approach and write a straightforward imperative solution it's
still very straightforward. In (deliberately non-idiomatic, so don't
whine at me) ruby:

~~~~ {language="ruby" name="code"}
sum_of_squares = 0sum = 01.upto 100 do |x|    sum_of_squares += x * x    sum += xendp (sum * sum) - sum_of_squares
~~~~
