post_id: Comment-Discontent
Author: DaStormyBlood
Date: 2008-07-30 18:03:00
Author_Email: noreply@blogger.com
Author_IP: None

The correct way to handle the square root issue, imho, is as follows: module foo.math; float NewtonRaphsonSquareRoot(); ... module bar.config; public import foo.math: sqrt = NewtonRaphsonSquareRoot; ... module bar.whee; import bar.config; ... sqrt(); ... And so on.
