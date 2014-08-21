post_id: Code-CAN-Be-Beautiful
Author: Jonathan Ville
Date: 2008-02-23 01:30:36
Author_Email: noreply@blogger.com
Author_IP: None

> Unfortunately, that's _not_ quicksort, but an out-of-order lazily evaluated <br />> mergesort equivalent. Quicksort is in-place.<br /><br />This is actually correct, and I think quite important to note. The function should be re-named &#39;msort&#39;.<br /><br />However, merge sort has an average and worse case time complexity of O(n log n). Quicksort has a lower bound of O(n log n) and upper bound of O(n^2), but in practice is very fast, if you have a randomized, fat pivot, and an un-sorted list.
