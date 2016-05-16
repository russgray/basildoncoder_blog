post_id: project-euler-problems-1-and-2
Author: Siddharth
Date: 2011-01-11 15:40:29
Author_Email: noreply@blogger.com
Author_IP: None

Hi,

Today i was introduced to the Euler project. Since im learning ruby now,
decided to use this to practice ruby...it is concise.

    :::ruby
    (1..999).select{|x| x%3==0 or x%5==0}.reduce(:+)
