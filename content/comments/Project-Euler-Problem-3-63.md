post_id: Project-Euler-Problem-3
Author: Meenakshi Sundaram
Date: 2010-08-02 15:09:45
Author_Email: noreply@blogger.com
Author_IP: None

Two while loops slow down the process in case the number is a prime. So one can replace the inner while loop as follows:<br />def primeFactors(n,factor):<br />factors=1<br />newn=n<br />while(factor*factor <= newn):<br />if(newn % factor !=0):<br />factor=factor+1<br />else:<br />factors=max(factors,factor)<br />newn=newn/factor<br />if(newn!=1):<br />factors=max(factors,newn)<br />return factors
