Title: Code CAN Be Beautiful
Date: 2008-02-22 17:57
Author: Russell Gray
Slug: Code-CAN-Be-Beautiful

In his [review](http://www.codinghorror.com/blog/archives/001062.html)
of *[Code Is Beautiful](http://www.amazon.com/gp/product/0596510047/)*,
Jeff Atwood decides that no, actually it isn't. He's fairly adamant
about it too:

> Ideas are beautiful. Algorithms are beautiful. Well executed ideas and
> algorithms are even more beautiful. But the code itself is not
> beautiful. The beauty of code lies in the architecture, the ideas, the
> grander algorithms and strategies that code represents.

I just can't agree with this. It's effectively saying that a
representation cannot be beautiful; only the underlying thing that's
*being represented* can be beautiful. Worse, this argument is extended
to literature and art as well, and quotes a reader review from Amazon
that quotes a little Russian poetry and rhetorically asks whether any
non-Russian-speaking reader can see beauty in it.

This drives me nuts, it really does. **Of course** the representation
can be beautiful, and it can also be ugly. And the beauty of the
representation can have an amplifying effect on the subject of the
representation. Form and content are related. A non-Russian-speaker may
not appreciate Russian poetry, but that doesn't mean that form itself
has no value - it means that, in this case at least, the value of form
is dependent on the content. If you don't understand the content, you
don't appreciate the form.

This isn't an absolute, though. In literature, there are many techniques
for adding value to form. Alliteration, assonance, metre, and many more
techniques are all structural techniques for beautifying form. I'd argue
that pretty much anyone can appreciate the compact and succinct beauty
of the phrase *veni, vidi, vici* without understanding what it means ("I
came, I saw, I conquered").

There are countless other examples. You don't need to understand Italian
to enjoy opera, for instance. In fact, I've even heard it argued that
understanding the content of an opera can diminish the experience, since
the actual meaning is often fairly bland and distracts from the simple
appreciation of the complex sounds and interplay of the language in the
hands (or lungs) of a world-class performer.

So what's the equivalent in software? I think expressiveness and
elegance are key. In particular, code that is able to express ideas
without adding a lot of noise. I'm very partial to Haskell for this sort
of thing - for instance the canonical quicksort implementation is
wonderfully precise:

    :::haskell
    quicksort []        = []
    quicksort (x:xs)    = quicksort less ++ [x] ++ quicksort greater
        where less      = [ y | y <- xs, y < x ]
              greater   = [ y | y <- xs, y >= x ]

If you know the quicksort algorithm, then the 2nd line of code there is
about as precise an expression of the underlying concept as you could
hope for. If you write the same algorithm in C or Visual Basic, I
believe that you can objectively distinguish the 'beauty' of these
representations of the same underlying concept. This is only possible if
the representations do indeed have the quality of beauty.

Another, perhaps even better, example is the naive-recursive Fibonacci
generator in the same language, which is remarkably close to the
mathematical definition:

![image](http://en.literateprograms.org/images/math/4/c/4/4c42de46d22d22305c59b9ba88e387e9.png)

(from
[literateprograms.org](http://en.literateprograms.org/Fibonacci_numbers_(Haskell)))

    :::haskell
    fib n
        | n == 0    = 0
        | n == 1    = 1
        | n > 1     = fib(n-1) + fib(n-2)

Note I haven't read the actual book under review here, and I have no
reason to doubt the assertions that the book doesn't deliver. I do,
however, take umbrage at the statement that code (or language) cannot be
beautiful.
