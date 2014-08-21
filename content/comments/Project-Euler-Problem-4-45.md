post_id: Project-Euler-Problem-4
Author: Sol
Date: 2008-04-23 11:53:25
Author_Email: noreply@blogger.com
Author_IP: None

Yeah, my thoughts on this seem to be muddled.  I think I have two issues.  <br /><br />It seems to me that the solution of converting the string to an array, reversing the array, then converting the array back to a string is both grotesquely inefficient and somewhat inelegant.  But on the flip side, it&#39;s dead easy to program quickly and be certain that you&#39;ve got it right.<br /><br />My corresponding instinct is that you should probably only be dropping into C if program efficiency is important.  So even though I&#39;d agree that your second C solution (in the next post) is probably the most elegant solution, my programming instincts look at it and go &quot;Ack!  Why is he doing the simple greater than check only after doing all the string manipulation?!&quot;<br /><br />I guess my overall instinct is that if programmer efficiency is of paramount importance, you shouldn&#39;t be working in C at all.  Combined with a slight layer of bitterness at all the very high level language advocates who are always trying to tell me that program efficiency isn&#39;t that important anymore, when in my work it is still crucial (and likely will remain so for at least another decade).  :)
