post_id: Code-CAN-Be-Beautiful
Author: Alan
Date: 2008-02-22 23:18:29
Author_Email: noreply@blogger.com
Author_IP: None

>Firstly, if you think code is beautiful, then:<br />><br />>qsort [] = []<br />>qsort (x:xs) = qsort (filter (= x) xs)<br />><br />>is a far more elegant implementation of quicksort, which essentially does the >same things as your list comprehensions, but in a more succinct way (list >comprehensions are implemented using filter and map anyway).<br /><br />I don&#39;t see how this will return anything except an empty list.  Is there something missing?
