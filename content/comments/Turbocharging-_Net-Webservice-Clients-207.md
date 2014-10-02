post_id: Turbocharging-_Net-Webservice-Clients
Author: russ
Date: 2008-09-11 17:22:27
Author_Email: noreply@blogger.com
Author_IP: None

Glyn,

I'm actually not sure what's going on there - the same thing is now happening
to me, but I can't figure out why. I think it's something at Betfair's end -
if I use the little python lib I cooked up, and switch on detailed tracing, I
see this (headers only):

    POST /global/v3/BFGlobalService HTTP/1.1
    Host: api.betfair.com:443
    Content-Length: 960
    SOAPAction: urn:getEvents
    Content-Type: text/xml
    Accept-Encoding: gzip
    User-Agent: pybetfair/0.4alpha

    HTTP/1.1 200 OK
    header: Server: Apache-Coyote/1.1
    header: Date: Thu, 11 Sep 2008 16:12:56 GMT
    header: Server: TME-GLUE/5.0.2
    header: Content-Type: text/xml;charset=UTF-8
    header: ntCoent-Length: 19715
    header: Cache-Control: private
    header: Content-Encoding: gzip
    header: Content-Length:       1498

So Betfair's servers definitely have compression switched on. It looks like
it's doing something weird with the headers (the jumbled ntCoent-Length header
contains the uncompressed size of the response), but the data is undoubtedly
compressed, and correctly represented in the Content-Length header. Weird.
I'll see if I can find out what's going on.

BTW, when using gzip, I believe only the response is compressed, not the
request.
