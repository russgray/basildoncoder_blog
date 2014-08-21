post_id: CSharp-3_0-Parallel-LINQ-And-The-Betfair-API-An-Introduction
Author: russ
Date: 2008-10-15 17:12:48
Author_Email: noreply@blogger.com
Author_IP: None

Hi Matt,<br /><br />The requirement that a unique session token be used for every single request was removed from the Betfair API some time ago. It is now possible to make many requests using a single token, and the temporal lifetime of a token is now quite long (not sure exactly how long, but I&#39;m pretty sure it&#39;s at least 24 hours). If you try the code above, you&#39;ll find it works fine.<br /><br />For long-running bots, however, it would certainly be the case that you&#39;d periodically need to overwrite the session token with a new one. I normally declare the session token variable to be volatile, share it between threads, update it with every response, and think no more about it. It is fine for multiple threads to use the same token, or for some threads to use an old token and others to use a new one, as long as any given thread doesn&#39;t try to use a token that has expired.
