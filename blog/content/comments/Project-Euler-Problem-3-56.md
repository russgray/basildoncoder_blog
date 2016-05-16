post_id: project-euler-problem-3
Author: -jn-
Date: 2008-04-20 01:09:18
Author_Email: noreply@blogger.com
Author_IP: None

Interesting! I learned a bit more Python by reading your post.

With respect to "only generate primes up to the square root of N", no fudge-
factor is needed. Simply keep track of the running quotient. After dividing 15
by 3 to get a quotient of 5, and verifying that 4 is > √15, you know that 5 is
prime.

It can't have two factors greater than √15 else it woud be > 15 itself. It
can't have a factor less than √15, because all of those factors have already
been eliminated.

Thanks for keeping it going!
