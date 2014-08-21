post_id: Project-Euler-Problem-3
Author: Meenakshi Sundaram
Date: 2010-08-02 14:43:30
Author_Email: noreply@blogger.com
Author_IP: None

sorry a correction <br />def primeFactors(n,factor):<br />factors=[]<br />newn=n<br />while(factor*factor <= newn):<br />while(newn % factor !=0):<br />factor=factor+1<br /><br />factors.append(factor)<br />newn=newn/factor<br />if(newn!=1):<br />factors.append(newn)<br />return factors
