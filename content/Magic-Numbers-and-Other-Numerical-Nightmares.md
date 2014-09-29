Title: Magic Numbers and Other Numerical Nightmares
Date: 2008-08-13 13:48
Author: Russell Gray
Slug: Magic-Numbers-and-Other-Numerical-Nightmares

There are many coding practices that are near-universally regarded as 'bad',
yet somehow keep cropping up over and over again. Conditional-branch abuse
(including, yes, gotos). Deep nesting. Cryptic variable names. Global
variables. Tight coupling. Entangled business/presentation logic. I could go
on.

Why do we keep doing it? Convenience? Laziness? Tiredness? Is unreadable
spaghetti code some sort of steady-state/equilibrium for code? Is it a natural
consequence of the vague and squidgy limitations of our evolved monkey-brains?
Or is well-designed code abhorred like a vacuum and naturally atrophies into
the sort of shambles you dread seeing on your first day at a new job, unless
well-intentioned and dedicated people actively work to clean and polish it,
like the [Forth
Bridge](http://en.wikipedia.org/wiki/Forth_Railway_Bridge#Maintenance)?

I don't have the time or wit to give this subject the treatment it deserves,
but I do want to rant a bit about another symptom of this disease, which has
given me a couple of sleepless nights recently. I refer, as the title might
suggest, to [magic
numbers](http://en.wikipedia.org/wiki/Magic_number_(programming)).

Magic numbers are constants, [unnamed](http://en.wikipedia.org/wiki/Magic_numb
er_(programming)#Unnamed_numerical_constant) in the most pathological cases,
that represent an assumption or a limit in a piece of code. They often cause
problems because soon they are forgotten about or their meaning is lost - and
then something happens to invalidate the assumption, the code breaks, and all
hell breaks loose.

Magic numbers, to stretch the definition a bit, can also be implicit. If you
are using a 32-bit integer, your magic number is 2,147,483,647 - that's the
biggest number you can store in that type. Often, movement up to and beyond
these ranges can trigger long-dormant bugs that are no fun at all to diagnose.

Three times in recent history I've been bitten by bugs of this class,
triggered by auto-incrementing sequences in database. These are they:

1. A table in a database had a 32-bit integer primary key. At the time this
seemed like a perfectly reasonable default, but insanely fast growth in usage
of the system meant that the ~2.1billion upper limit of that data type was
quickly reached. The DB column was switched to a 64-bit integer, but some of
the client applications reading that table were not identified as at-risk.
When the sequence generator left the 32-bit range, those applications
overflowed. This happened at 4:30pm on a Friday afternoon. Saturdays were
peak-times for system usage. You can imagine the frantic hacking that ensued.

2. A sequence generator for a particular entity was started at 20,000,000, so
as not to clash with the ID sequence of a related entity (that had started at
0 a good few years earlier). The similarity between the entities and the need
to not have the IDs overlap had valid business justification, but the magic
number was selected arbitrarily and promptly forgotten. Inevitably, the latter
sequence surpassed that number, causing bizarre and difficult-to-trace entity
relationship corruption that manifested as strangely-disappearing data on the
front-end.

3. A stored procedure parameter was incorrectly declared as an
OracleType.Float, when it should have been an OracleType.Int32. This resulted
in the value being cast from an integer to a floating-point and back again.
For the first 16,777,216 integers, this happens to work OK. For the value
16,777,217, however, the loss in precision means that the number changes
during casting. This simple bit of (heavily contrived) code shows the problem:

        :::csharp
        static void Main(string[] args)
        {
            for (int i = 0; i < 17000000; ++i)
            {
                if (i != (int)(float)i)
                {
                    Console.WriteLine("{0} != {1}", i, (int)(float)i);
                    break;
                }
            }
        }

    There are many numbers above 16,777,217 that have this characteristic;
    16,777,217 just happens to be the first, for reasons you can probably
    divine if you think the IEEE floating-point spec is a riveting read. A
    couple of weeks after the launch of a fairly major internal application,
    this time-bomb exploded due to a sequence reaching the magic number. The
    bug was nothing to do with the new application, but of course fingers were
    pointed at it since a long-running and stable system had mysteriously
    choked very shortly after deployment of the new application.

Now, unquestionably, all these problems are avoidable, and a strong argument
could be made that none of them should ever have been allowed to happen. Yet,
for many reasons, they do. For example, first-mover advantage can mean the
opportunity cost of taking the time to do things right first time is greater
than the cost of fixing problems later.

Also, people make assumptions. The issue underlying the [Millennium
Bug](http://en.wikipedia.org/wiki/Millennium_bug) hysteria was caused by well-
meaning developers who knew that two-digit dates wouldn't work after 1999
(effectively another magic number), but assumed the software would have been
replaced or upgraded by then. No doubt that seemed a totally reasonable
assumption in the 1970s, and it had genuine technical benefits (storage space
was so tight that every byte saved was a battle won).

Anyway, I don't have a magic bullet solution for this, I'm just venting
spleen. Unit tests can help, but won't magically eliminate this class of bug
(no matter what some of the more extreme TDD fanatics might tell you), so I
suppose the lesson to take from this is the importance of being able to
recognise and diagnose potential magic number issues. Pay close attention to
data types, type conversions, and current values of sequences in your
database. Keeping a sacrifical goat on hand might pay dividends too, in case
any blood-thirsty deities with a head for binary arithmetic are watching.
