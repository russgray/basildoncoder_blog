post_id: Project-Euler-Problem-3
Author: Meenakshi Sundaram
Date: 2010-08-02 14:43:30
Author_Email: noreply@blogger.com
Author_IP: None

sorry a correction

    :::python
    def primeFactors(n,factor):
        factors=[]
        newn=n
        while(factor*factor <= newn):
            while(newn % factor !=0):
                factor=factor+1

        factors.append(factor)
        newn=newn/factor
        if(newn!=1):
            factors.append(newn)
        return factors
