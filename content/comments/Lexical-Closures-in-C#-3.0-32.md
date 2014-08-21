post_id: Lexical-Closures-in-C#-3.0
Author: Russ Gray
Date: 2013-06-11 14:55:20
Author_Email: noreply@blogger.com
Author_IP: None

Yeah, at some point I wrote the code using List<t>, which <a href="http://msdn.microsoft.com/en-us/library/bwabdf9z.aspx" rel="nofollow">does</a> have a ForEach method, but for some reason switched it to an array for this blog post without re-testing it. My bad. Either change funcs to a List<func> or implement ForEach as an extension for IEnumerable, which is trivial. Or, as you say, use a normal loop.</func></t>
