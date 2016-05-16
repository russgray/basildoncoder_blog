post_id: project-euler-problem-3
Author: Thebigcheeze
Date: 2011-04-15 16:58:08
Author_Email: noreply@blogger.com
Author_IP: None

Check into using the BitArray class for your C# implementation.  It's meant
for holding large volumes of binary data.  Obviously, it can't hold everything
(69.9GB) but you gain an 8x datasize improvement over using booleans (assuming
booleans use 1 byte per bool).
