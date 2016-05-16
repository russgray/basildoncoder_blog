post_id: code-can-be-beautiful
Author: Weave Jester
Date: 2008-02-22 23:39:45
Author_Email: noreply@blogger.com
Author_IP: None

> 	qsort [] = []
> 	qsort (x:xs) = qsort (filter (= x) xs)
>
> is a far more elegant implementation of quicksort

The comment system ate everything between the less-than and greater-than operators. Hopefully this will come out right:

	:::haskell
	qsort [] = []
	qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++ qsort (filter (>= x) xs)