post_id: Project-Euler-Problems-1-and-2
Author: Hugh Redelmeier
Date: 2008-03-24 19:03:28
Author_Email: noreply@blogger.com
Author_IP: None

Problem 1 seems to be quite efficiently solved in the standard UNIX bc program.  O(1) (ignoring the fact that bc uses arbitrary precision numbers).<br />  $ bc<br />  define s(n) { return n * (n + 1) / 2 }<br />  define t(n,m) { return s((n - (n % m)) / m) * m }<br />  t(999,3) + t(999,5) - t(999,15)<br />  233168<br />  quit<br /><br />s(n) is the sum of the integers 1 to n, inclusive.<br />t(n,m) is the sum of all the integers that are multiples of m between 1 and n, inclusive.<br />The problem answer is the (sum of multiples of three) + (sum of multiples of five) - (sum of multiples of 15 since they would have been counted twice).<br /><br />Your C# program would choke if you changed 1000 to a googol.  The BC program says:<br />23333333333333333333333333333333333333333333333333333<br />33333333333333333333333333333333333333333333333166666<br />66666666666666666666666666666666666666666666666666666<br />66666666666666666666666666666666666666668<br />I haven&#39;t checked if that is correct. but it has about the right number of digits.
