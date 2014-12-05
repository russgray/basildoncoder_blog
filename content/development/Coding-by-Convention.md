Title: Coding by Convention
Date: 2007-12-09 20:00
Author: Russell Gray
Slug: coding-by-convention
Tags: ruby, coding

I've been meaning for a while to have a play around with [Ruby on Rails][1],
on the basis that anything generating so much hype over the last year or two
deserves some level of investigation, if only to see whether the hype is
justified. So, I spent a couple of days working through [*Agile Web
Development with Rails*][2] and, well, it's pretty nice. I can certainly
appreciate a development environment that goes to such endearing effort to do
work for you without getting in the way - a fairly tricky balancing act. I
came to the book with a working knowledge of Ruby but zero practical exposure
to Rails, and on top of that I'm not a web developer so could not bring much
contextual experience to the table. Despite this, I worked through the book
and ended up with a functional book-store application in about 15 hours. Not
too shabby.

So how does Rails achieve such power and productivity? The answer is largely
that Rails, more so than pretty much any other development environment I've
used, leverages the power of convention. That is, if you stay 'on rails' and
behave the way Rails wants you to, then in return you get a great deal of
functionality for free. A kind of technological "you scratch my back, and I'll
scratch yours". If you structure your application as Rails expects, then Rails
will automatically hook everything up for you. If you name your database
tables as Rails wants you to, and create the primary/foreign key id columns
that Rails expects, then Rails will take care of all your object-relational-
mapping needs for you. Sounds like a good deal, yes?

Rails doesn't expect you to jump through all these hoops yourself though. It
provides a number of useful scripts that you can use to perform the common
tasks you want to do, in the way that Rails wants you to do them. Probably the
best example of this is when you first start a new project. You ask Rails to
create an application for you, with the name you specify, then off it goes -
and creates 45 files in 37 directories, without you having to lift a finger.

    :::bash
    $ rails dummy
          create
          create  app/controllers
          ...
          ...
          create  log/development.log
          create  log/test.log
    $ find dummy/ -type f |wc -l
    45
    $ find dummy/ -type d |wc -l
    37

Compare this to a newborn ASP.Net application created using the Web Site
wizard in Visual Studio 2005:

    :::bash
    $ find WebSite1/ -type f |wc -l
    2
    $ find WebSite1/ -type d |wc -l
    2

A pretty substantial difference. And if you stay within the confines of Rails'
expectations when adding to the project - which is very easy to do since you
are provided with more generators for creating models, controllers, and
migrations (basically incremental DB deployment scripts) - then you end up
with a nicely structured application in accordance with the hallowed
principles of MVC design, and everything is glued together automatically.
Create a new data model, and your controller is immediately able to load it
from the database along with all its relational buddies in a nice aggregated
object structure with just one line of code (as long as you remembered to add
all the `has_many` and `belongs_to` calls, of course). Store that data object
in a controller member variable, and your views can access it for display. Use
one of the magical rake incantations and get a DB-backed session management
system which will horizontally scale in a load-balanced environment. Run the
script/console script and you are dropped into a fully interactive command-
line environment similar to irb, where you can instantiate and interact with
all your objects dynamically. Tail the development log and you can see all the
generated SQL as it is executed, and even get indicated performance in terms
of theoretical request-per-second capacity. It's all just fab. Nothing
spectacularly new, of course; each individual feature has been done before,
but Rails pulls them all together very nicely indeed.

As I worked through the aforementioned book, however, it was very clear that
without the guiding instruction of the esteemed Dave Thomas and DHH I'd be up
the creek without a paddle, and that got me thinking. Programming by
convention is all great and frictionless and wonderful *as long as you know
the conventions*. Imagine, if you will, the sheer blank incomprehension of a
maintenance programmer who's never heard of Rails, sitting down to tweak a
Rails application.

Wait, what? How can this happen? Surely everyone has heard of Rails by now?
Nope, sorry, but the truth is that the [majority of programmers][3] are clock-
punchers living in a single-language world who don't read blogs, or play
around with tech in their own time, and haven't even heard of Linux, let alone
Rails. Their single language will likely be an everyday static language like
Java or C#, which will leave them ill-prepared for many of the dynamic tricks
in idiomatic Ruby.

Ah, but surely the kind of forward-thinking proto-company that builds its
product on RoR would never hire non-Ruby-savvy developers anyway? That might
be the case if you drink the [37signals][4] Kool-Aid and think that any RoR
company is by default über-smart and infallible, but in the real world it
doesn't work like that; there are countless tiny non-technical companies out
there with just one or two developers - I know, because I spent a few years
working at one - and maybe their current developers are cool enough to use
RoR, but when they inevitably leave and the tech-illiterate management hire a
replacement, you can guarantee that the job spec will not include minor
details like "must have at least heard of Ruby on Rails".

So, our imaginary maintenance guy - let's call him Ted - hired by a non-
technical company to look after a web application, peers for the first time
into the 37 directories (assuming no new ones have been added) and >45 files
(since new ones will most certainly have been added), and nothing makes any
sense. Even assuming Ted is smart enough to make reasonable guesses about Ruby
syntax, and knows what MVC is, there's no visible link between the different
layers of the application. It isn't clear how data is shuttled to and from the
database. It isn't clear why things don't always work as expected when Ted
tries to manually add new things, rather than using the Rails scripts (which
he doesn't know about), even when diligently trying to emulate the structure
and layout of existing code. It all seems like sorcery. What is Ted to do?

The correct answer is to go and by a Rails book of course, or at least try and
pick out the decent tutorials on the web (unfortunately, there's a lot more
chaff than wheat in this area, maybe a sign that Rails is becoming a bit more
mainstream?). A few days of getting up-to-speed, and Ted achieves
enlightenment and becomes mega-productive, and lives happily ever after. So
coding by convention is a good thing, right?

Maybe.

I'm still uneasy about sorcery, and Rails is some of the most effective
sorcery I've seen. The main problem is that, well, it's sorcery. A couple of
times in the 15 hours I spent going through [*Agile Web Development with
Rails*][5] I hit problems. Not major ones, and always of my own making - some
silly typo, or mistake coming from only having a working knowledge of Ruby
rather than cosy familiarity. As is my wont, failure to spot the error after a
cursory glance through the code led to a quick google search to see if I've
hit a common problem, before resigning myself to going through the code in
detail to sort it out (like all good programmers I'm a lazy devil).

On these periodic google jaunts I found lots and lots of forum posts and blog
entries from people who, and let's not mince words here, hadn't the first clue
what they were doing. People that had heard the Rails hype, bought the book
(and probably the t-shirt), hit problems, and were now running around like a
cargo cult expecting magic spells to solve all their problems. Restart
WEBrick. rake db:sessions:clear. Roll the most recent migration back then
forward again. None of these work? Sorry, can't help. It reminds me of [The IT
Crowd][6]'s "have you tried turning it off and on again?".

I shouldn't be harsh on these folks; at least they're getting excited by Rails
and are rolling up their sleeves and having a go, and no doubt some of them
will succeed wildly and become far better, richer, more attractive programmers
than I can ever hope to be. Also let me be clear that I think the productivity
gains of software like Rails is a good thing, and Rails is certain to account
for a good chunk of my tinkering time for the next few months. It worries me,
however, when people try to run before they can walk, and the magic of coding
by convention tends to encourage it.

I'll leave it as an exercise for the reader to consider the implications of
the fact that the sample application being conjured here by all these
sorcerers' apprentices is an e-commerce site, at a time when online fraud is
[skyrocketing][7].

I don't mean to single out Ruby on Rails specifically, by the way, it's just
handy as an example due to its profile. Coding by convention is not new; if
you want an older example of what happens when people are given programming
tools that allow them to get something working - for fairly loose definitions
of 'working' - without knowing much about what's happening under the hood,
then look at the atrocities committed with VB and databinding over the years.

Steve Yegge has a characteristically long and insightful [rant][8] on this
subject, and is troubled by the difficulty of working out where to draw the
line. The line, in this case, being the level of abstraction at which a
programmer should understand a system - high enough not to be bogged down in
insane detail (e.g. knowing how semiconductors work) but not so high that the
role of programmer is reduced to that of sideshow conjurer, waving a cheap
trick-shop wand and trusting to a higher power that everything will work out
OK.

Maybe it's just a generational disease. Maybe in ten years' time all the
apprentices who have graduated to fully-fledged sorcerers will be looking on
in dismay at the young scamps creating Web 5.0 applications using Ruby on
MagLev simply by burping commands into their Skype headsets, and writing
cautionary blogs about the dangers of not knowing how to write a partial web
template.

Theoretically, a perfect system - perhaps a descendant of Rails in the dim and
distant future - would contain such exquisitely crafted assumptions and such
frictionless conventions that it would never go wrong and always do the right
thing. Thus, the need to understand anything at the lower level of abstraction
required to sort out any problems is obviated, unless you are one of the very
few Grand High Wizards who keep everything running smoothly. I don't know
whether it's fortunate or unfortunate that such a system is unlikely to appear
within my lifetime.


[1]: http://www.rubyonrails.org/
[2]: http://www.amazon.co.uk/Agile-Development-Rails-Pragmatic-Programmers/dp/0977616630/
[3]: http://www.codinghorror.com/blog/archives/001002.html
[4]: http://www.37signals.com/
[5]: http://www.amazon.co.uk/Agile-Development-Rails-Pragmatic-Programmers/dp/0977616630/
[6]: http://en.wikipedia.org/wiki/The_IT_Crowd
[7]: http://news.bbc.co.uk/1/hi/business/6298641.stm
[8]: http://steve.yegge.googlepages.com/practical-magic