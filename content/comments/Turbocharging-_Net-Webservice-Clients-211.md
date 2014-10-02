post_id: Turbocharging-_Net-Webservice-Clients
Author: TheBotanist
Date: 2010-06-28 11:54:06
Author_Email: noreply@blogger.com
Author_IP: None

i have been caught out by this, my thread pool (10 threads) has been beavering
away placing bets, on the surface it looks ok. The reality is only 2 threads
have ever been calling the api concurrently.

This was highlighted when I was making lots of bets on an in play match - the
5 second delay highlighted the fact that calls were being serialized ie they
were backing up. As a result I got timout exceptions which caused me to
research and ended up here.. I will implement all these suggestions - these
are excellent easy wins for a performace boost coding againt the betfair API.
