post_id: pg-wodehouse-method-of-refactoring
Author: Rob Fagen
Date: 2008-03-24 02:47:17
Author_Email: noreply@blogger.com
Author_IP: None

@Dan: You make a perfectly reasonable, compelling and completely internally
@consistent argument. However, I think that you're arguing for something
@almost but not completely unlike the problem driving the original post.

An application can be close to the metal or close to the people using it.
Applications close to the metal need to be horrendously fast and efficient
because they are doing things that people can't do fast enough because of the
size or complexity of the data. An application close to the people using it is
something that is keeping track of something too complex for a person to
reliably do repeatedly.

My impression of your work is 'optimization uber alles.' Which is a cool space
to be working in from a computer science perspective. My impression of the
work everyone else is discussing is that it's much closer to the rest of the
world than it is to the hardware. Which is also cool, but from more of a
holistic business perspective. At a certain point, it becomes much more
important to be able to reliably change what's going on inside the application
than it is for the application to run as quickly as is mathematically
possible.

At work, we have a ginormous pile of PL/SQL with a lot of business logic
buried in it. It was put there back in the day because the best minds at the
time thought it was important to be as fast as possible. It was as fast as
possible at the time, because the data from the database didn't need to make
the round-trip to and from the application server for a given transaction. It
has become a problem today because of how business logic has become
implemented across both the application server and the database. We're
untangling it, but it's going to cost at least three engineers the better part
of a year to do that untangling because of all the interdependencies and the
fact that this is a 24x7 system.

Being able to think about the problem with your feet in the world of the
people consuming the information is sometimes much more valuable than thinking
about the problem with your feet in the world of the machine consuming the raw
data.
