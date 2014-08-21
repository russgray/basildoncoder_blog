post_id: Lexical-Closures-in-C#-3.0
Author: mabra
Date: 2010-02-12 23:33:43
Author_Email: noreply@blogger.com
Author_IP: None

Hi !<br /><br />I am just dealing with captured variables in creating Tasks and came onto the same idea [using a local variable, copying the loop vars value].<br /><br />Just don&#39;t work and return different results on each run!<br /><br />BTW, I find lambda&#39;s too abstract and cannot understand them. So you also?<br /><br />Your code:<br />funcs.ForEach(f => Console.WriteLine(f()));<br />does not compile ....<br />[No overload for method &#39;ForEach&#39; takes &#39;1&#39; arguments]<br /><br />br--mabra
