post_id: Lexical-Closures-in-C#-3.0
Author: Mark Giese
Date: 2013-06-11 14:18:57
Author_Email: noreply@blogger.com
Author_IP: None

Don&#39;t know where &quot;funcs.ForEach&quot; is coming from, but the following replacement works.  The main point of the article is important and certainly not invalidated by the typo.<br /><br />            foreach (Func f in funcs)<br />            {<br />                Console.WriteLine(f());<br />            }<br />
