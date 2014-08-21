post_id: Turbocharging-_Net-Webservice-Clients
Author: russ
Date: 2008-09-11 17:27:09
Author_Email: noreply@blogger.com
Author_IP: None

elmariachi,<br /><br />The new .Net 3.5 Add Service wizard (using WCF) seems to have gone out of its way to make this difficult. When I use 3.5, I always create 2.0-style web references. There are two ways to do this:<br /><br />1) Use wsdl.exe directly (e.g. from the command line or a build script<br /><br />2) In VS2008, in the Add Service Reference dialog, click Advanced... (bottom left corner), then click Add Web Reference... in the Service Reference Settings dialog that pops up. You should then be able to use EnableDecompression as usual.
