post_id: Project-Euler-Problems-1-and-2
Author: Brian
Date: 2011-06-16 02:22:55
Author_Email: noreply@blogger.com
Author_IP: None

I like it in python:

    :::python
    sum([i for i in range(1000) if not (i%5 and i%3)])

or with a generator instead

    :::python
    sum((i for i in range(1000) if not (i%5 and i%3)))
