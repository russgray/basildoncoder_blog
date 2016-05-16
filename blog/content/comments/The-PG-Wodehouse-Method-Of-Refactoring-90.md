post_id: pg-wodehouse-method-of-refactoring
Author: Kristofer
Date: 2008-03-23 09:55:41
Author_Email: noreply@blogger.com
Author_IP: None

I think it is unfair to say that a "total rewrite" always fail. I think the
issues are approached from the wrong angle.

The ambition is seldom to copy a complex program but to re-invent it with the
accumulated knowledge of its core business functions. Nothing would be gained
from 'copying' since as you suggest, you'd probably just reintroduce old bugs
because of copy-mistakes. Refactor works better because you are moving towards
a goal implicitly defined by the couplings in your program; -The program code
has an inertia and 'seeds' of programming groups follow the law of least
resistance. If the over all program was a result of a set of business
requirements, chances are good the program will converge against an optimized
image of those business requirements.

But.. It should be possible to short cut this traditional evolution by more
accurately control the seeds and better describe the _models_ of business
requirements, thus enable a faster 'rewrite' of the code to fit a slimmer set
of business requirement with higher market value and better margins. Such a
process would be preferred because it would enable the business producing the
code to be much more agile. Remember the Dodo: Perfect evolution but stuck on
the same track.

What would it look like? Probably a dual model with one aspect looking like
groups of independent teams responsible for code fragments which are subject
to regular refactoring, and the other aspect would be programs exchanging
these fragments as they 'mate' to produce a business service. This is the
nature of service-oriented and open source business... So, "rewrite" fails
because of the clumsy approach of a product-oriented business and the lack of
an agile short-cutting strategy (ie thow everything and start over)
