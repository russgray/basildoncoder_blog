post_id: Project-Euler-Problem-3
Author: Meenakshi Sundaram
Date: 2010-08-02 15:09:45
Author_Email: noreply@blogger.com
Author_IP: None

Two while loops slow down the process in case the number is a prime. So one
can replace the inner while loop as follows:

    :::python
    def primeFactors(n,factor):
        factors=1
        newn=n
        while(factor*factor <= newn):
            if(newn % factor !=0):
                factor=factor+1
            else:
                factors=max(factors,factor)
        newn=newn/factor
        if(newn!=1):
            factors=max(factors,newn)
        return factors
