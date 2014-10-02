post_id: Project-Euler-Problem-6
Author: wrf3
Date: 2008-08-30 16:07:30
Author_Email: noreply@blogger.com
Author_IP: None

To continue with ASk's line of thought:

The sum of the first n numbers is:

    1 + 2 + 3 + ... + n = n^2/2 + n/2

The sum of the squares of the first n numbers is:

    1^2 + 2^ + 3^2 + ... + n^2 = n^3/3 + n^2/2 + n/6

So another solution to the problem is:

    (n^2/2 + n/2)^2 - (n^3/3 + n^2/2 + n/6)

or, simplified,

    n^4/4 + n^3/6 - n^2/4 - n/6
