post_id: code-can-be-beautiful
Author: gwenhwyfaer
Date: 2008-02-22 19:40:54
Author_Email: noreply@blogger.com
Author_IP: None

&quot;If you know the quicksort algorithm, then the 2nd line of code there is about as precise an expression of the underlying concept as you could hope for.&quot;

Unfortunately, handing it a pre-sorted list will demonstrate the gulf between beauty and practicality.

In any case, since Haskell&#39;s data structures are immutable, mergesort is a much better match for it; the only advantage of qsort is that it can execute in-place - which...