Title: Comment Discontent
Date: 2008-07-30 17:01
Author: Russell Gray
Slug: comment-discontent

There seems to have been a recent [outbreak][1] [in][2] [blog][3] [posts][4]
about [code commenting][5]. As is so often the case with topics such as this,
everyone has an opinion and they all seem to be different. It's quite an eye-
opener seeing some of the explanations, justifications, and outright
haranguing used in defence of all sorts of weird and wonderful stances.

I got a wry smile from [stevey's post][6], as I recognise only too well the
tendency to write narrative comments. I'm sure there's plenty of code from
early in my career still floating around in various company codebases where
the code/comment ratio is something embarrassing. I've mostly shaken that off
now, though I sometimes have to fight my inner raconteur when writing
something I think is neat or clever.

Jeff Atwood, as is so often the case recently, contradicted his [own previous
post][7] on the matter (replacing the statement "comments can never be
replaced by code alone" with "if your feel your code is too complex to
understand without comments, your code is probably just bad") and endearingly
veered wildly to and fro across a sensible medium[^1], without ever quite
hitting it. Coding Horror, indeed.

So far, so blah; every time an argument on comments flares up we see the same
thing. Something I've not noticed before though, either because I wasn't
paying attention or because it's a new thing, is a trend amongst the I-don't
-need-comments crowd to advocate very long and detailed method names as an
alternative.

As neophyte coders we all have it drilled into us that we must use descriptive
names. Programming gospel, as handed down in sacred tomes such as [Code
Complete][8], tell us not to use names like 'i' and 'tmp' except in very
specific circumstances (e.g. loop indexes and tempfile handles). And, without
question, this is good solid advice. Take heed, young Padawan, etc.

But can you take it too far? It's not something I've really come up against,
but it seems to be increasingly popular. [One response][9] to Jeff's post
suggested (only in passing, to be fair) using a function name like
`newtonRaphsonSquareRoot`. A digg comment (OK, OK, not exactly the fount
of all knowledge) vehemently defended the virtue of the frankly- scary
`RunEndOfMonthReportsUnlessTheMonthStartsOnAFridayInWhichCaseRunTheWeekl
yReportInstead` (!)

The argument is that with names like these, you don't need comments, since it
is perfectly clear what the function does. Is it perfectly clear at the wrong
level though? Function names like this, in my opinion, are so 'clear' that
they leak. These are function names that violate the principle of
[encapsulation][10].

If I write a square root function, why do I need to burden all my clients with
information about how I've implemented it? By naming it
`newtonRaphsonSquareRoot`, that's exactly what I'm doing. Unless there are
specific performance implications/requirements that favour [Newton-
Raphson][11], in most cases my clients just want a damn square root calculated
to within a specified tolerance and don't care whether I used Newton's method
or one of the [army of alternatives][12]. The implementation should be private
to the method, and no-one else's business.

Worse, what if a requirements change means a switch to [Walsh's fast
reciprocal method][13]? Uh-oh, now my method name is completely misleading, so
I have to change it. Oops, now I have to change all the client code that calls
it! I'd better hope no-one has exposed this with `[WebMethodAttribute]` since
I wrote it, otherwise there could be thousands of client applications out
there relying on it. My funky rename refactoring can't save me now.

If every tiny change propagates through the system requiring hundreds of
source files to change, and possibly external apps as well, you may as well
just copy 'n' paste the code everywhere it's needed and doing away with the
function completely. Hell, who needs abstraction anyway?

We all do, of course, which is why I think names like this are a bad smell.
The same goes for `RunEndOfMonthReportsUnless...` - what happens when the
requirements change? This method name couples the public interface (method
name) to the private implementation, which is exactly what you're not supposed
to do. `RunEndOfMonthReports` is probably sufficient. Separate interface and
implementation. This is programming 101, people, it shouldn't be beyond our
grasp.

[^1]: I agree with [Dan Dyer][14] that the best choice is as follows:

        :::java
        /**
         *  Approximate the square root of n, to within the specified
         *  tolerance, using the Newton-Raphson method.
         */
        private double approximateSquareRoot(double n, double tolerance) {
            double root = n / 2;
            while (abs(root - (n / root)) > tolerance) {
                root = 0.5 * (root + (n / root));
            }
            return root;
        }

The function name is descriptive and clear whilst remaining general enough to
allow an alternative implementation. Anyone who cares enough about the
implementation (for performance reasons, or simply curiosity) can find enough
information in the comment to start their investigation, without having the
details jammed in their face every time they call it.


[1]: http://blog.uncommons.org/2008/07/25/no-your-code-is-not-so-great-that-it-doesnt-need-comments/
[2]: http://www.carlcrowder.com/blog/?p=34
[3]: http://www.codinghorror.com/blog/archives/001150.html
[4]: http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html
[5]: http://en.wikipedia.org/wiki/Comment_(computer_programming)
[6]: http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html
[7]: http://www.codinghorror.com/blog/archives/000749.html
[8]: http://www.amazon.co.uk/Code-Complete-Practical-Handbook-Construction/dp/1556154844
[9]: http://blog.uncommons.org/2008/07/25/no-your-code-is-not-so-great-that-it-doesnt-need-comments/
[10]: https://en.wikipedia.org/wiki/Encapsulation_(object-oriented_programming)
[11]: http://en.wikipedia.org/wiki/Newton%27s_method
[12]: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
[13]: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Reciprocal_of_the_square_root
[14]: http://blog.uncommons.org/2008/07/25/no-your-code-is-not-so-great-that-it-doesnt-need-comments/