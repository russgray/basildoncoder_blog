post_id: Turbocharging-_Net-Webservice-Clients
Author: russ
Date: 2008-02-24 19:48:17
Author_Email: noreply@blogger.com
Author_IP: None

Hi Joann, thanks for the comment. Hope the tips come in useful!

It is an interesting point about the use of web services for such a high
performance application. However, I happen to know that XML
serialisation/deserialisation is the largest bottleneck in the system from
Betfair's perspective, so I'm not sure XMPP would help much.

For pure performance, a custom binary protocol would be superior, but then you
have the additional burden of writing and maintaining the protocol, and can
run into all sorts of interesting problems with byte ordering and encoding
across different platforms and processor architectures. Interoperability is
the trump card here.
