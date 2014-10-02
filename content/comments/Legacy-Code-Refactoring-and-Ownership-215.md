post_id: legacy-code-refactoring-and-ownership
Author: russ
Date: 2007-12-15 21:28:02
Author_Email: noreply@blogger.com
Author_IP: None

> I bring this to your attention so as not to continue the proliferation of
> mythology and mislead potentially innocent bystanders into a similar state
> of delusion.

The phrase "everyone knows that" was intended to be slightly tongue-in-cheek,
which I had hoped would be picked up by being unnecessarily sweeping and all-
encompassing. Generally speaking I think it's a good thing, but I also think
Steve Yegge hit the nail on the head when he said that refactoring had become
the [goal rather than the cure][1].

I read your [Refunctoring][2] article and largely agree with it; I code C# for
a living and often find myself edging towards a functional style for certain
problems. However, I think you're a bit strident; not all refactoring is
simply a progression towards using map, foldr, and filter; similarly, I think
you're overly harsh on Java and C#. C# at least is moving in interesting
directions - LINQ is providing something very similar to (if more verbose
than) Haskell's list comprehensions, and also now supports lambdas and a form
of type inference. Whilst it's never going to be as much fun writing C# as it
is to write Haskell or Ruby (which are my preferred languages outside the
office, along with Ocaml), it's encouraging that such a mainstream language is
starting to "get it".

I hold my hand up and concede that my phrasing didn't really communicate any
of this. Sorry. I'm just getting used to blogging and realise I need to be
careful about how people interpret my writing.


[1]: http://steve.yegge.googlepages.com/transformation
[2]: https://tonymorris.github.io/blog/posts/refunctoring/