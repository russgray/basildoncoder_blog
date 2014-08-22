post_id: Code-CAN-Be-Beautiful
Author: Jonathan Ville
Date: 2008-02-22 19:45:23
Author_Email: noreply@blogger.com
Author_IP: None

Firstly, if you think code is beautiful, then:

	:::haskell
	qsort [] = []
	qsort (x:xs) = qsort (filter (= x) xs)

is a far more elegant implementation of quicksort, which essentially does the same things as your list comprehensions, but in a more succinct way (list comprehensions are implemented using filter and map anyway).

Secondly, the reason this is &#39;beautiful&#39; has nothing to do with the elegant syntax and much more to do with the fundamental ideas behind functional programming, and the maths used to show that the lower assymptotic bound of the running time is n log n (which is analysis of algorithms - a beautiful subject). And of course, there&#39;s always the fantastic proofs by induction you can do in functional programming.

And I bet you can&#39;t write a functional program that finds fibonacci numbers much faster using matrix multiplication (and diagonalisation of matrices to make this fast). The maths behind that is truly beautiful.

There is good syntax and bad syntax, but at the end of the day syntax is transient and a bad way to judge a language.