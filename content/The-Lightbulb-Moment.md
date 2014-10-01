Title: The Lightbulb Moment
Date: 2008-03-25 18:06
Author: Russell Gray
Slug: The-Lightbulb-Moment

[Weiqi Gao][1] has a
[post][2]
up today discussing the trials of grokking
[Scala][3]. Scala is a language I want to take
a much closer look at later this year, since I want to become current on
the [JVM][4] again
(having not been on talking terms with it since using J2SE 1.4 around
the summer of 2003) without being particularly keen on tangling with the
Java language itself.

One of the key features of Scala is the functional programming style it
brings to the JVM. It's actually quite common to use certain functional
idioms in Java - e.g. passing around a function as a parameter - but the
syntax is clunky and verbose (unless and until closures get confirmed in
1.7, that is, and maybe even then).

For example, take a look at this very simple idiomatic code for spinning
off a thread to perform an expensive operation:

    :::java
    new Thread (new Runnable() {
        public void run() {
            someObj.doExpensiveOperation();
        }
    }).start();

Now that's not the most hideous code I've ever seen, but it's a
bit...wordy. Compare it to this equivalent implementation in Java's
closest mainstream relative, C#:

    :::csharp
    new Thread(x => someObj.DoExpensiveOperation()).Start();

I much prefer this syntax, even taking into account the throwaway lambda
parameter that's only there to satisfy the ThreadStart signature. The
Scala syntax is even nicer, however:

    :::scala
    spawn({ someObj.doSomethingExpensive })

This is the sort of thing that piques my interest about the language -
expressive syntax and a very funky concurrency model will get my
attention, *especially* when running on something as mainstream as the
JVM and with full interoperability with the frankly staggeringly-vast
Java library ecosystem. I like F# on the
[CLR][5] for similar
reasons.

But I digress; what I wanted to talk about was a point made by Weiqi,
when discussing the pattern-matching capabilities of Scala:

> Pattern matching in Scala is exactly the point at which I would spend
> time trying to understand it, trying to master it, trying to learn to
> use it. I understand the syntax. I understand the explanation that the
> speakers in presentations gave. I do get to the part where I say "This
> is cool." But I never get to the point where I would see a problem and
> say "This problem is best solved with pattern matching, let me fire up
> Scala and code the solution."

This strikes a chord for me, as I have gone through that stage once or
twice myself with other features in other languages and yet can't quite
put my finger on how I get past it. I don't think it's something you
consciously do - it's just something you keep grafting away at until
suddenly you realise that the technique, whatever it is, has become part
of your armoury.

Closures are an obvious example I can think of in my own background. I
was raised as a straight-down-the-middle C++ man, way back in the
early/mid-90s, cutting my teeth on Borland Turbo C++ 3 on Windows 3.1.
When I first started to play with functional languages it took a long
time for me to 'get it', and even when I understood what a closure was
after a couple of weekends hacking around in OCaml, I couldn't envisage
when I'd ever need one.

Soon after, whilst working on a Konfabulator widget in javascript, I
noticed I was using them all the time. I suddenly had much more insight
into what ruby blocks were doing. It wasn't so much that I noticed the
lights go on - *they'd been on for some time* and I hadn't realised.

People commonly refer to the 'lightbulb moment' or 'the lights went on'
as being the point where a flash of inspiration hits and everything
suddenly makes sense. I don't like this metaphor. If I need to go to the
bathroom in the middle of the night, when the lights go on I squint in
pain and stagger around just as blindly as I did before. But then I
acclimatise, and all becomes clear. And so it is, I think, with learning
alien concepts - you need a bit of time to adjust to the dazzling light.


[1]: http://www.weiqigao.com/blog/
[2]: http://www.weiqigao.com/blog/2008/03/24/scala_still_uncomfortable_after_five_years.html
[3]: http://www.scala-lang.org/
[4]: http://en.wikipedia.org/wiki/Java_Virtual_Machine
[5]: http://en.wikipedia.org/wiki/Common_Language_Runtime