post_id: The-PG-Wodehouse-Method-Of-Refactoring
Author: David Barrett
Date: 2008-03-23 18:26:16
Author_Email: noreply@blogger.com
Author_IP: None

I've found that there are situations where a rewrite actually is preferable.
In particular, if you are rewriting with the aim of *reducing* functionality
and *eliminating* complexity, then it can work.  But if you trying to
*increase* functionality and *add* complexity (optimizations, flexibility,
etc), then you'll probably fail.

Contrary to popular belief, it really doesn't take long to write code.  It
just takes long to debug it.  It's easier to debug a small set of simple code
that you wrote from the ground up, than debug a huge set of nasty code that
you're actively refactoring.  Even if it means you're just re-encountering the
same general domain problems that coders solved before you, I'd rather take
those problems (at least I have a working reference to consult!) than take an
entirely new set of implementation-specific problems in code I barely
understand.

Using these ideas, I and 2 others rewrote a p2p client and 6 servers in 6
weeks (from the beaches of Thailand, no less -- http://blog.redswoosh.net),
and -- this is the kicker -- deployed it to 20 servers and several hundred
thousand clients.  And it worked!  It was scary, but one of the best decisions
we made, as I spent the previous six *months* trying to refactor through
intense pain and significant complications (many of which, unfortunately,
affected users and customers).

So don't get caught up in religion: sometimes a rewrite is the way to go,
especially if your goal is to do *less* than what you started with.
