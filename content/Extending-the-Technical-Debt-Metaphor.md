Title: Extending the Technical Debt Metaphor
Date: 2008-02-21 16:07
Author: Russell Gray
Slug: Extending-the-Technical-Debt-Metaphor

A few months ago, the inestimable Steve McConnell (he of *[Code
Complete](http://www.amazon.co.uk/Code-Complete-Practical-Handbook-Construction/dp/0735619670/)*
fame)
[wrote](http://blogs.construx.com/blogs/stevemcc/archive/2007/11/01/technical-debt-2.aspx)
about [technical
debt](http://www.martinfowler.com/bliki/TechnicalDebt.html). McConnell
looks to extend the metaphor beyond the simple idea of 'code that is
going to be a liability in the future', identifying two main types of
technical debt (deliberate and accidental), and identifying further
correlations between the worlds of financial debt and technical debt.

For instance, based on the technical debt already accumulated, one team
may have a worse 'credit rating' than another:

> Different teams will have different technical debt credit ratings. The
> credit rating reflects a team's ability to pay off technical debt
> after it has been incurred.
>
<cite>(McConnell, 2007)</cite>

There is a lot of insight in McConnell's article, and I recommend you
nip over and read it right now if you haven't already. Technical debt is
indeed a useful and rich analogy for communicating a particular class of
technical problem to non-technical users.

I wonder, however, if McConnell hasn't extended the metaphor in slightly
the wrong direction. When considering technical debt, I like to think of
the product managers as the debtors, and the development team as the
creditors. The actual underlying concept remains the same, it's just a
shift in responsibilities.

Why?

As a developer, I don't always get to make the decisions about whether
something should be done in a quick 'n' dirty hack, or a
properly-architected solution. Of course, I'm likely to recommend the
latter where I can, but it's a fact of life that I will often be
overruled, and rightly so. There are occasions when incurring technical
debt is the right thing to do. McConnell lists a few examples, e.g:

> *Time to Market*. When time to market is critical, incurring an extra
> $1 in development might equate to a loss of $10 in revenue. Even if
> the development cost for the same work rises to $5 later, incurring
> the $1 debt now is a good business decision.
>
<cite>(McConnell, 2007)</cite>

This is a key issue. Software development considerations are not the
be-all and end-all, no matter how much I (or any other developer) would
like them to be. It's the *product teams* that make these business
decisions, however, and therefore **it should be the product teams that
incur the debt**.

As developers, **we are the ones who give the product guys what they
want, and we take on the risk of that debt not being repaid**, and
that's why we are the creditors.

So what does this mean? It means that, when considering whether to
create some additional technical debt, it's the product team that should
have a credit rating. Have they been making quick-win decisions
excessively over the last six months? Well then, maybe they're at their
*credit limit*, and cannot incur any more debt until they have used some
of their budget on a project that reduces debt.

How about if a product manager hasn't incurred any debt recently, but
made a load of bandito decisions on a major project a year ago, and now
the codebase is starting to feel the impact? Charge them *interest* on
the debt, so that now it will cost more of their budget to pay off their
debt. This is entirely fair, since with a longstanding debt it is often
the case that more code has been built on top of it in the interim,
which may have been written well but is inherently unstable due to the
shaky foundations. Paying off the debt in full will involve refactoring
this new code, too.

Of course, you need a fairly enlightened product team if this metaphor
is to be accepted, not to mention significant buy-in from senior
management if you are seriously at risk of jeopardising the product
roadmap by sticking to your guns. However, since the technical debt
metaphor is something of a meme at the moment, why not suggest it? If
the technical debt metaphor really does improve understanding on the
part of non-technical stakeholders, maybe it isn't a hopeless daydream
that they'll also accept the logical extensions of the idea.
