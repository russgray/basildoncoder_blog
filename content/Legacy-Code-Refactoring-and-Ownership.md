Title: Legacy Code, Refactoring, and Ownership
Date: 2007-12-13 17:26
Author: Russell Gray
Slug: Legacy-Code-Refactoring-and-Ownership
Tags: coding, refactoring, software engineering

Refactoring is good. Everyone knows that. Since Fowler popularised the concept
with the seminal [*Refactoring: Improving the Design of Existing Code*](http://www.amazon.co.uk/Refactoring-Improving-Design-Existing-Technology/dp/0201485672/) it's become a staple of the industry, and has pride
of place on many a bookshelf. In the many, many articles and discussions of
the subject, the key goals and benefits of refactoring are generally taken to
be the improvement of readability, testability, decoupling, and other similar
worthy ideals. For me, however, there is another very distinct benefit, often
overlooked. Fowler touches upon it, but doesn't really develop it, early on in
*Refactoring*:

> I use refactoring to help me understand unfamiliar code. When I look at
unfamiliar code, I have to try to understand what it does. I look at a couple
of lines and say to myself, oh yes, that's what this bit of code is doing.
With refactoring I don't stop at the mental note. I actually change the code
to better reflect my understanding, and then I test that understanding by
rerunning the code to see if it still works.
>
<cite>(Fowler, *Refactoring*, 1999)</cite>

By investigating a piece of code thoroughly enough to understand how it works,
refactoring it to map directly on to your understanding, and reinforcing
everything with good unit tests, you take *ownership* of the code. It's yours
now.

This is very important, psychologically. Almost every developer feels more at
home with their own code than somebody else's. That's why you feel
uncomfortable and deflated when, 20 minutes into deciphering a nasty bit of
opaque gibberish, you realise it was something you yourself wrote a year
earlier and subsequently forgot about.

When you refactor, you rewrite code to a greater or lesser extent. Having done
so, the resulting feeling of ownership (alongside increased understanding, of
course) makes the code much less scary. The benefit of this is less marked in
agile methodologies or TDD, of course, since in those cases quite often the
code you are refactoring was written by you anyway. Working with legacy code,
though, it's a big deal.

In the preface to 
[*Working Effectively With Legacy Code*](http://www.amazon.co.uk/Working-Effectively-Legacy-Robert-Martin/dp/0131177052/), Feathers asks "what do you think about when you hear
the term *legacy code*?" (Feathers, 2004). He answers by stating that the
standard definition is "difficult-to-change code that we don't understand" and
adds his own preferred definition which is, in essence, "code without tests".

My own definition of legacy code would include, in many cases, code that
*isn't mine*. By 'mine' I don't exclusively mean code I wrote personally; I
also mean code written by my team, or even code written by people who sit a
couple of desks down who I can go and pester about it (which is stretching the
definition a bit, admittedly).

In short, legacy code for me is code that no longer has any accessible owner.
Like a stray cat or dog, code without an owner goes feral. Refactoring is the
process of taming feral code, but as with stray cats much of the benefit comes
from re-homing. This is a vital process, even if a fairly unconscious one.
When you first come face to face with some hideous 5000-line spaghetti monster
of a function your heart sinks - how can anyone ever hope to understand that,
let alone modify it safely? Especially if the only people that ever worked
with it left the company 3 years ago?

Refactoring allows you to split this code up, create classes to better
represent the problem domain, improve abstraction, add tests, and all that
other good stuff; at the same time, the process of doing so makes the code
yours. You make the decisions about the classes to create and the abstractions
to introduce. You write the tests that ferret out all the little
idiosyncrasies, and uncover the unwritten assumptions. By the end of the
process, the code feels like yours. And that means that the next time you have
to make a change there, you benefit from the double whammy of code that is not
only well-written and tested, but recognisably *yours*; and that's the kind of
code that you won't mind working with.
