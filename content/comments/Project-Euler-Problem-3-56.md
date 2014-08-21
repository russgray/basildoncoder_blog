post_id: Project-Euler-Problem-3
Author: -jn-
Date: 2008-04-20 01:09:18
Author_Email: noreply@blogger.com
Author_IP: None

Interesting! I learned a bit more Python by reading your post.<br /><br />With respect to &quot;only generate primes up to the square root of N&quot;, no fudge-factor is needed. Simply keep track of the running quotient. After dividing 15 by 3 to get a quotient of 5, and verifying that 4 is > √15, you know that 5 is prime.<br /><br />It can&#39;t have two factors greater than √15 else it woud be > 15 itself. It can&#39;t have a factor less than √15, because all of those factors have already been eliminated.<br /><br />Thanks for keeping it going!
