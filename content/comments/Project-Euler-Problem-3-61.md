post_id: Project-Euler-Problem-3
Author: Meenakshi Sundaram
Date: 2010-08-02 14:37:41
Author_Email: noreply@blogger.com
Author_IP: None

A slightly modified version. I have avoided the use of recursion.

    :::python
    def primeFactors(n,factor):
        factors=[]
        newn=n
        while(factor*factor <= newn):
            while(newn % factor !=0):
                factor=factor+1

            factors.append(factor)
            newn=newn/factor
            if(factor!=1):
                factors.append(newn)

            return factors
