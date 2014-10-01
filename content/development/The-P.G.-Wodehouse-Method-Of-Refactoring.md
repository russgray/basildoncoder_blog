Title: The P.G. Wodehouse Method Of Refactoring
Date: 2008-03-21 23:01
Author: Russell Gray
Slug: The-PG-Wodehouse-Method-Of-Refactoring

I am much given to ruminating on refactoring at the moment, as one of my
current projects is a major overhaul of a fairly large (>31,000 lines)
application which has exactly the kind of dotted history any experienced
developer has learned to fear - written by many different people, including
short-term contractors, at a time in the company's life when first-mover
advantage was significantly more important than coding best-practice, and
without any consistent steer on the subjects of structure, coding conventions,
unit tests, and so on.

In other words, here be dragons.

In fairness, the application *works* and has been a critical part of a company
that has gone from nothing to market-leading multinational in 7 years, so it
has certainly pulled its weight. It is in desperate need of a spring-clean
though, and my team volunteered to spend 3 months evicting the cobwebs and
polishing the brasswork.

Yes, *volunteered* - it's a fascinating challenge, though perhaps not
something you'd want to make a career of.

Now, the first mistake to avoid here is the compulsion to throw it away and
rewrite from scratch. So often when confronted with a vast seething moiling
spiritless mass of code a developer throws his hands into the air and declares
it a lost cause. **How seductive is the thought that 31,000 lines of code
could be thrown away and replaced with ~15,000 lines of clean, well-designed,
[beautiful code][1]?**

Sadly, that's often a path to disaster. It's almost a rule of the game.
[jwz][2] left Netscape because he knew their decision to rewrite from scratch
was doomed. [Joel Spolsky][3] wrote a [rant][4] about the same decision - in
fact, the Netscape rewrite is commonly cited as a major factor in Netscape
losing the first browser war.

**The problem is that warty old code isn't always just warty - it's *battle-
scarred*.** It has years of tweaks and bug-fixes in there to deal with all
sorts of edge conditions and obscure environments. Throw that out and replace
it with pristine new code, and you'll often find that a load of very old
issues suddenly come back to haunt you.

So, a total rewrite is out. This means working with the old code, and finding
ways to wrestle it into shape. Naturally, *[Working Effectively With Legacy
Code][5]* now has an even more firmly established place on my 'critical books'
bookshelf than it did before.

Inspiration came from a less well-known book, however. Buried in Chapter 10 of
*[Code Reading][6]* is a single paragraph suggesting that it can be useful
when working with unfamiliar code to paste it into a word processor and zoom
out, getting a 'bird's eye' view.

> One other interesting way to look at a whole lot of source code
> quickly under Windows is to load it into Microsoft Word and then set
> the zoom factor to 10%. Each page of code will appear at about the
> size of a postage stamp, and you can get a surprising amount of
> information about the code's structure from the shape of the lines.
>
<cite>(Spinellis, 2003)</cite>

The idea is that this lets you immediately identify potential trouble spots -
if you see pages where the code is all bunched up on the right, it indicates
massive nesting and over-long functions. If you see heavy congestion, it
indicates dense code. It's also easy to spot giant switch statements and other
crimes against humanity.

Of course, you don't actually need MS Word to do this - the Print Preview in
Open Office is more than sufficient, and no doubt most office suites can do
the same.

![image][7]

This 50,000ft view could be a useful tool in tracking progress. I mean sure,
we can have our build system spit out [cyclomatic complexity][8] and code size
metrics, but wouldn't it be neat if we could do a weekly bird's-eye printout
of the source code and pin it up on the wall, giving a nice simple visual
representation of the simplification of the code?

Except, of course, that with average page lengths of 45 lines we'd need almost
700 pages each time, and a hell of a lot of wall space.

A better solution would be to print a class per page. At the start of the
project, the application had about 150 classes, and the refactoring effort is
focussed on about 80 of those. Initially, gigantic classes would be an
incomprehensible smudge of grey, but as the refactoring process starts tidying
the code and factoring out into other classes, **the weekly printout would
start to literally come into focus**, hopefully ending up with many pages
actually containing readable code (which happens roughly when the class is
small enough to fit on no more than 3 pages at normal size).

The first time we pinned up the printouts, I suddenly recalled a Douglas Adams
foreword reprinted in *[The Salmon of Doubt][9]*. Adams was a great fan of
P.G. Wodehouse, and explained Wodehouse's interesting drafting technique:

> It is the next stage of writing—the relentless revising, refining, and
> polishing—that turned his works into the marvels of language we know
> and love. When he was writing a book, he used to pin the pages in
> undulating waves around the wall of his workroom. Pages he felt were
> working well would be pinned up high, and those that still needed work
> would be lower down the wall. His aim was to get the entire manuscript
> up to the picture rail before he handed it in.
<cite>(Adams, 2002)</cite>

Hmm, isn't redrafting a literary cousin of refactoring? In many ways, I think
it is - so **why not apply this technique to refactoring?**

And we've made it so. We tied a piece of string horizontally across the wall -
that's our 'picture rail'. Every week we reprint the classes we have been
working on, and replace the old printouts. Then we move them up towards the
string, in accordance with how happy we are with the view.

Obviously, this doesn't replace all the other tools we have for evaluating
code quality - e.g. the aforementioned metrics, unit tests, manual QA, and so
on. It does, however, make for a brilliant way of tracking our
*subjective*satisfaction with the class. **Software quality tools can never
completely replace the gut instinct of a developer** - you might have massive
test coverage, but that won't help with subjective measures such as [code
smells][10]. With Wodehouse-style refactoring, we can now easily keep track of
which code we are happy with, and which code we remain deeply suspicious of.

As an added benefit, all those pages nicely cover up the hideous wall
colour. Bonus!


[1]: {filename}/commentary/Code-CAN-Be-Beautiful.md
[2]: http://www.jwz.org/
[3]: http://www.joelonsoftware.com/
[4]: http://www.joelonsoftware.com/articles/fog0000000069.html
[5]: http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052
[6]: http://www.amazon.co.uk/Code-Reading-Perspective-Effective-Development/dp/0201799405
[7]: {filename}/images/print-preview-birds-eye-view.png
[8]: http://en.wikipedia.org/wiki/Cyclomatic_complexity
[9]: http://www.amazon.co.uk/Salmon-Doubt-Hitchhiking-Galaxy-Last/dp/0330323121
[10]: http://en.wikipedia.org/wiki/Code_smell