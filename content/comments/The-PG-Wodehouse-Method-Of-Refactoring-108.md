post_id: The-PG-Wodehouse-Method-Of-Refactoring
Author: Tim Daly
Date: 2008-03-23 20:32:55
Author_Email: noreply@blogger.com
Author_IP: None

Here's another suggestion. Use literate programming. (see Knuth).

I refer you to the excellent book "Lisp in Small Pieces".  You might not care
about Lisp but this is an excellent  example of literate programming.

Rewriting the program in literate form has two useful effects. First, in order
to explain the code in some logical manner you end up "tree shaking the code",
that is, you start somewhere, write up section 1 of chapter 1, and then start
following the threads from there, gradually moving code from the original
files into the new book. Dead code will never get moved. Second, you end up
having to write a lucid explanation of the code which forces you to explain.
In order to develop the explanation you need to understand. With understanding
comes the ability to rewrite and refactor.

You eventually end up with an extremely well documented piece of code that
anyone can sit down and read like a book; at which point your chair-rail
metric is exact.

Tim Daly
