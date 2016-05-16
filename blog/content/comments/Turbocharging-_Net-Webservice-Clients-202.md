post_id: turbocharging-net-webservice-clients
Author: David
Date: 2008-05-19 20:56:11
Author_Email: noreply@blogger.com
Author_IP: None

Everything works great except when the web service throws an Exception the
client receives "The remote server returned an error: (500) Internal Server
Error."  With decompression turned off the client receives our normal
customized application exceptions and we can trap them appropriately.  Is
there something else we need to implement when overriding WebResponse so the
client receives our custom exceptions?  The 500 error is thrown at
request.GetResponse() in the HttpWebResponseDecompressed constructor.

Great article btw.
