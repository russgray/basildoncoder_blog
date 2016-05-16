post_id: lexical-closures-in-c-30
Author: Russ Gray
Date: 2013-06-11 14:55:20
Author_Email: noreply@blogger.com
Author_IP: None

Yeah, at some point I wrote the code using List<T\>, which [does][1] have a
ForEach method, but for some reason switched it to an array for this blog post
without re-testing it. My bad. Either change funcs to a List<Func\> or
implement ForEach as an extension for IEnumerable, which is trivial. Or, as
you say, use a normal loop.


[1]: http://msdn.microsoft.com/en-us/library/bwabdf9z.aspx
