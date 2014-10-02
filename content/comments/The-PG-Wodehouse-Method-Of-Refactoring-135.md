post_id: The-PG-Wodehouse-Method-Of-Refactoring
Author: Michael Elliot
Date: 2008-03-27 16:57:28
Author_Email: noreply@blogger.com
Author_IP: None

If we all could agree that domain specific knowledge and particulars of actual
applications greatly dictate the manners by which code refactoring should be
done, that would be great.

In general what's typically missing in code is why certain code exists.  This
is very hard to capture without reasonably accurate coding standards and
designs.  Keeping roles and responsibilities highly consistent helps to keep
the code in this state and doing this requires constant refactoring of even
more recently written code. (Of course this is for projects whose lifeline is
in the 5 - 10 year arena, which is crazy, but true for certain machine control
applications)

And yes, I agree a big picture certainly does help see where code and
complexity reign.  If done correctly, this would happen when multiple
interfaces must be integrated within a single class/entry point.

I've spent my entire career refactoring code that functions at ~75% case, but
fails in a large set of other cases.  Typically it is because these junction
points are either poorly designed, written, or missing altogether.  Not to
belittle the idea of looking at something from 10,000 feet, but isn't that
what UML is all about?
