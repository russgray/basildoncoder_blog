post_id: comment-discontent
Author: Thomas Eyde
Date: 2008-08-24 20:37:17
Author_Email: noreply@blogger.com
Author_IP: None

It's possible to use method names as comments without breaking encapsulation

    public double SquareRoot(double n)
    {
        //return NewtonRaphsonSquareRoot(n);
        return WalshFastReciprocalSquareRoot(n);
    }

    private double NewtonRaphsonSquareRoot(double n)
    {
        ...
    }

    private double WalshFastReciprocalSquareRoot(double n)
    {
        ...
    }
