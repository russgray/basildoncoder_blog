post_id: The-PG-Wodehouse-Method-Of-Refactoring
Author: Tim Daly
Date: 2008-03-23 20:32:55
Author_Email: noreply@blogger.com
Author_IP: None

Here&#39;s another suggestion. Use literate programming.<br />(see Knuth).<br /><br />I refer you to the excellent book &quot;Lisp in Small Pieces&quot;. <br />You might not care about Lisp but this is an excellent <br />example of literate programming.<br /><br />Rewriting the program in literate form has two useful<br />effects. First, in order to explain the code in some logical<br />manner you end up &quot;tree shaking the code&quot;, that is, you<br />start somewhere, write up section 1 of chapter 1, and then<br />start following the threads from there, gradually moving<br />code from the original files into the new book. Dead code<br />will never get moved. Second, you end up having to write<br />a lucid explanation of the code which forces you to explain.<br />In order to develop the explanation you need to understand.<br />With understanding comes the ability to rewrite and refactor.<br /><br />You eventually end up with an extremely well documented<br />piece of code that anyone can sit down and read like a book;<br />at which point your chair-rail metric is exact.<br /><br />Tim Daly
