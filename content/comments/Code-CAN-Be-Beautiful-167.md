post_id: Code-CAN-Be-Beautiful
Author: russ
Date: 2008-02-22 21:11:21
Author_Email: noreply@blogger.com
Author_IP: None

>Firstly, if you think code is beautiful, then:
>
>	:::haskell
>	qsort [] = []
>	qsort (x:xs) = qsort (filter (= x) xs)
>
>is a far more elegant implementation of quicksort, which 
>essentially does the same things as your list comprehensions, 
>but in a more succinct way (list comprehensions are implemented 
>using filter and map anyway).

Actually, I prefer the one I posted. Probably a subjective thing, but I find mine maps more directly onto how I conceptualise the algorithm in my head. But hey, as so many people have already said, beauty is in the eye of the beholder, right? Also, I agree with you that syntax is a bad way to judge a language, but that&#39;s not really what I&#39;m trying to do here. Haskell&#39;s qualities as a language don&#39;t really influence my perception of certain Haskell snippets as &#39;beautiful&#39;.