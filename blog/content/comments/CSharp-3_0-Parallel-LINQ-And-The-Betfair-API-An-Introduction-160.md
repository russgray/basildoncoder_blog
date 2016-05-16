post_id: c-30-parallel-linq-and-betfair-api
Author: russ
Date: 2008-10-15 17:12:48
Author_Email: noreply@blogger.com
Author_IP: None

Hi Matt,

The requirement that a unique session token be used for every single request
was removed from the Betfair API some time ago. It is now possible to make
many requests using a single token, and the temporal lifetime of a token is
now quite long (not sure exactly how long, but I'm pretty sure it's at least
24 hours). If you try the code above, you'll find it works fine.

For long-running bots, however, it would certainly be the case that you'd
periodically need to overwrite the session token with a new one. I normally
declare the session token variable to be volatile, share it between threads,
update it with every response, and think no more about it. It is fine for
multiple threads to use the same token, or for some threads to use an old
token and others to use a new one, as long as any given thread doesn't try to
use a token that has expired.
