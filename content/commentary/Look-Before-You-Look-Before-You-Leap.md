Title: Look Before You Look Before You Leap
Date: 2008-10-24 15:32
Author: Russell Gray
Slug: Look-Before-You-Look-Before-You-Leap

Generally, I try to avoid turning this blog into some sort of [snark][1]-fest
about other programmers or blogs. I've disagreed with Jeff Atwood [once][2] or
[twice][3] though, and so by posting this I'm probably straying a little close
to the edge...but what the hell.

A couple of days ago Coding Horror carried a [fluff piece][4] about how all
developers should be marketers too. Predictably, the article soon got posted
to [proggit][5] where it was [ripped on by reddit's resident Jeff-haters][6],
and even more predictably the comments were a mix of interesting insight and
barely-concealed hate.

Apparently some of them got up Jeff's nose a bit, and today he [responded][7].
The core of his rebuttal seems to be that you shouldn't trust what you read on
blogs, and should verify everything yourself. True enough, I guess, if perhaps
a bit impractical given the sheer amount of information out there.

Then, however, Jeff goes on to give an example by referencing a [compression
benchmark][8] he'd read on a blog and providing counter-analysis to show that
the benchmark was wrong in claiming Deflate is faster than gzip. In doing so,
much knowledge was gained.

Or so we are told.

The comment thread quickly becomes a goldmine of humour. Bugs in Jeff's
benchmarking code (not resetting the stopwatch) meant that the durations were
cumulative, not independent, with inevitable distortion of the results.
Another commenter pointed out that [gzip][9] cannot possibly be faster than
Deflate, since the gzip algorithm IS the Deflate algorithm plus some
additional computation.

> “gzip” is often also used to refer to the gzip file format, which is:
>
> -   a 10-byte header, containing a magic number, a version number and
>     a timestamp
> -   optional extra headers, such as the original file name,
> -   a body, containing a DEFLATE-compressed payload
> -   an 8-byte footer, containing a CRC-32 checksum and the length of
>     the original uncompressed data
>
<cite>([Wikipedia][10]</cite>

With the benchmarking code fixed, we see that Deflate is indeed slightly
faster than gzip.

All of which leads to repeated quotations from Jeff about the community being
smarter than him, and some drastic toning down of language in post-publication
edits to the article. I read a cached version of the RSS feed, which is
markedly different to the article currently live on codinghorror.com - "on my
box, GZip is twice as fast as Deflate" becomes "on my box, GZip is just as
fast as Deflate", "Deflate is way slower. It's not even close" becomes
"Deflate is nowhere near 40% faster", etc.

![Coding Horror screengrab][11]

Anyone who's tackled a major performance problem will likely agree that
profiling is a tremendously valuable technique that should always be
applied before attempting to optimise (i.e. look before you leap). I
think this little episode has highlighted a couple of important things
to bear in mind, however:

1. Profiling isn't a magic wand - if you use buggy profiling code, you are
leading yourself up the garden path.

2. Profiling is less useful when you can reason (in the mathematical sense)
about the code. That involves *understanding the algorithms you are dealing
with*. Gzip is Deflate plus a bit more processing - so unless that extra
processing has a negative duration gzip must necessarily take longer. You
don't need a profiler to work that out. Look *before*you look before you leap.

Anyway, enough hatcheting from me, normal service will be resumed
shortly.


[1]: http://www.google.co.uk/search?q=define%3Asnark
[2]: {filename}/commentary/Code-CAN-Be-Beautiful.md
[3]: {filename}/commentary/Freedom-Zero--The-All-Or-Nothing-Fallacy.md
[4]: http://www.codinghorror.com/blog/archives/001177.html
[5]: http://www.reddit.com/r/programming/
[6]: http://www.reddit.com/r/programming/comments/78vq3/jeff_atwood_finally_jumps_the_shark/
[7]: http://www.codinghorror.com/blog/archives/001178.html
[8]: http://blog.madskristensen.dk/post/Compression-and-performance-GZip-vs-Deflate.aspx
[9]: http://en.wikipedia.org/wiki/Gzip
[10]: http://en.wikipedia.org/wiki/Gzip)
[11]: {filename}/images/codinghorror01.png