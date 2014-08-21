post_id: Code-CAN-Be-Beautiful
Author: Weave Jester
Date: 2008-02-22 23:39:45
Author_Email: noreply@blogger.com
Author_IP: None

> qsort [] = []<br />> qsort (x:xs) = qsort (filter (= x) xs)<br />><br />> is a far more elegant implementation of quicksort<br /><br />The comment system ate everything between the less-than and greater-than operators. Hopefully this will come out right:<br /><br />qsort [] = []<br />qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++ qsort (filter (>= x) xs)
