post_id: Project-Euler-Problem-4
Author: russ
Date: 2008-04-23 15:19:26
Author_Email: noreply@blogger.com
Author_IP: None

Again, you're right in all details, I just think we're looking at it through
slightly different lenses. I worked on embedded software for a few years so I
do have some exposure to areas where efficiency is paramount, and it still
does crop up in desktop and web development (which is where I earn a crust
these days), so I'd never claim it's completely irrelevant. In fact, maybe
part of the reason I'm not pandering to it here is because I'm indulging
myself by ignoring it ;-)

Regarding the choice of C in this post, if you look at some of the other posts
in the series you'll see that I often do a straightforward imperative solution
first, as to most developers that is still the most recognisable form. I chose
C here partly in line with that, and partly on a whim - but not because I had
performance (or lack of it) in mind. I haven't written any C code in anger for
a couple of years, and this seemed like a good chance to review some of the
basics.

The string reversal/comparison stuff was simply the first straightforward
solution that popped into my head. It was also convenient in that it was an
approach that would work in most other languages, whereas mutating the string
with pointers is a bit less universal :-)
