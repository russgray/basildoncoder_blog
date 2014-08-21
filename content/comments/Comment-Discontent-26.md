post_id: Comment-Discontent
Author: Thomas Eyde
Date: 2008-08-24 20:37:17
Author_Email: noreply@blogger.com
Author_IP: None

It&#39;s possible to use method names as comments without breaking encapsulation:<br /><br />public double SquareRoot(double n)<br />{<br /> //return NewtonRaphsonSquareRoot(n);<br /> return WalshFastReciprocalSquareRoot(n);<br />}<br /><br />private double NewtonRaphsonSquareRoot(double n)<br />{<br /> ...<br />}<br /><br />private double WalshFastReciprocalSquareRoot(double n)<br />{<br /> ...<br />}
