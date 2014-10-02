Title: OOD - The Second Coming
Date: 2009-01-16 16:00
Author: Russell Gray
Slug: ood-second-coming

Over the last couple of months I've been burning up my free time on a pet
project (hence the scarcity of posting here). This particular project is a web
application, and since I've always been a desktop or middle-tier dude in my
day job, it's a bit of a step out of my normal environment to grapple with
browser compatibility and suchlike.

Still, I wanted it to be a decent learning experience, so after a brief
dalliance with Rails I scrapped the idea of using any [framework sorcery][1]
and decided to write everything in plain ol' [PHP][2], and lean heavily on
[YUI][3] and [jQuery][4] to sort out the browser stuff.

This probably isn't an approach I'd use in future projects, but I bet I'll
appreciate those frameworks a lot more once I've encountered and understood
the problems they attempt to solve.

So, having strayed from the comfort of [Rails][5] and its clones, I had to
think about lots of things like security, validation, data access, and how to
organise my code. Just because I'd abandoned the training wheels I had no
intention of falling over all the time - I still wanted a nice, maintainable
app with sensible abstractions, properly decoupled, and resilient to failure.
Time to start reading articles and the odd open source project, obviously.

It's at this point I noticed something interesting. Since I regularly read
plenty of development websites it could scarcely have escaped my notice that
the trendy framework players (e.g. Rails, Django, Cake, ASP.NET MVC) strongly
advocate the [MVC][6] pattern and [class-based object-oriented design][7].
What I hadn't really realised until now is how endemic that viewpoint had
become.

In fact, beyond a few admirably out-there frameworks like [Seaside][8], it's
almost universal. OOD = good, EVERYTHING ELSE = bad. MVC = good, EVERYTHING
ELSE = bad. No shades of grey, no room for dissenting opinion.

Go anywhere where best-practices are discussed and mention you're writing some
procedural code, and watch the fireworks. It doesn't matter if your
application has fewer lines of code than a newly-created Rails app has source
files - if you haven't structured it with models, views, and controllers you
may as well have written it in Visual Basic for all the bile you're going to
have thrown at you.

If you say you're writing functional code, you might get away with it, since
functional programming is still widely misunderstood and you'll likely be
classified as some weird LISPer or Schemer doing something arcane and thus
ignored.

Ironically, of course, if you grab a random Rails/Django/Cake app from
[github][9] or [Google Code][10], there's a pretty fair chance that what
you'll find isn't particularly object-oriented anyway. Hint - usage of the
'class' keyword does not an object-oriented design make. And sweet zombie
Jesus, I've never seen such abuse of the singleton pattern. That's a sure sign
someone doesn't 'get' OO - the [singleton pattern is evil][11] and basically a
way to [shoehorn globals into an application][12] without admitting it to your
friends.

So, we have massive fanatical advocacy of a technique that will allegedly
solve all your problems, coupled with large-scale real-world misunderstandings
and misapplication. Does this remind anyone of anything? Say, for example, the
last time OOD swept the world, panacea to all programming woes, about 20 or so
years ago?

Don't get me wrong, I'm not arguing that class-based OO itself is just a fad -
it deserves its place as a paradigm alongside procedural, functional,
parallel, and numerous others. It's the heralding of OO as the one true way
that seems faddish.

So, in the very best "bah, humbug" traditions I've written my app in
unashamedly procedural PHP code. I don't mix my presentation and content. My
data layer is decoupled and unit tested. Every bit of SQL is a parameterised
query, to guard against injection. I don't have a single echo() statement
containing any html tags. All my errors are exception based, and I don't have
a single die() call anywhere. My average function size is about 10 lines, and
my longest is about 20. I've no doubt that there's a legion of 15-year-old
self-appointed geniuses ready to accuse me of inflicting yet more spaghetti
code junk on the world just because "find . -iname '*php' | xargs grep class"
comes up empty, but hey I'm OK with that.

I'm writing my next app in [brainf*ck][13]
using ed.


[1]: {filename}/development/Coding-by-Convention.md
[2]: http://php.net/
[3]: http://developer.yahoo.com/yui/
[4]: http://jquery.com/
[5]: http://rubyonrails.org/
[6]: http://en.wikipedia.org/wiki/Model-view-controller
[7]: http://en.wikipedia.org/wiki/Class-based_programming
[8]: http://www.seaside.st/
[9]: http://github.com/
[10]: http://code.google.com/hosting/
[11]: http://c2.com/cgi/wiki?SingletonsAreEvil
[12]: http://steve.yegge.googlepages.com/singleton-considered-stupid
[13]: http://en.wikipedia.org/wiki/Brainfuck