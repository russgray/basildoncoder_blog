post_id: CSharp-3_0-Parallel-LINQ-And-The-Betfair-API-An-Introduction
Author: Matt
Date: 2008-10-15 08:04:44
Author_Email: noreply@blogger.com
Author_IP: None

Hi,

Your application of PLINQ to this scenario is good, however I&#39;m a little confused how the session with the BF API is maintained.

My understanding is that the Session Token from each Response needs to be passed in to each subsequent Request to ensure the session is maintained with the API.

How would this be achieved when multiple calls are made to the API concurrently? (I realize that you can spin up multiple sessions but there is a maximum limit imposed per user account so I wouldn&#39;t think that to be a viable solution). Am eager to hear your response.

Thanks,
Matt
