Title: MySQL 'Table not found' Error When Referring To A New Table In A Trigger
Date: 2012-12-18 11:31
Author: Russell Gray
Slug: mysql-table-not-found-error-when

Note to self - the following bullet point from the MySQL docs applies to new
tables as well as modified tables.

> The trigger cache does not detect when metadata of the underlying objects
> has changed. If a trigger uses a table and the table has changed since the
> trigger was loaded into the cache, the trigger operates using the outdated
> metadata.
<cite>[MySQL docs][1]</cite>

Do not hot-deploy a new table and a trigger update to refer to it, bad
things will happen.


[1]: http://dev.mysql.com/doc/refman/5.6/en/stored-program-restrictions.html