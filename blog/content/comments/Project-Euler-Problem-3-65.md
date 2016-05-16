post_id: project-euler-problem-3
Author: lolpium
Date: 2010-10-18 18:10:17
Author_Email: noreply@blogger.com
Author_IP: None

Hey I'm very much a beginner but was pretty stoked I could run this in 3164ms.
Heres the code --

    #The prime factors of 13195 are 5, 7, 13 and 29.
    #What is the largest prime factor of the number 600851475143?
    import os, sys, math, sets, time

    time1 = time.clock()
    iniList = []

    var = 600851475143

    def factorize(num):
    templist = []
    max = int(math.sqrt(num))
    print "max = ",max
    i = 1
    while i m and i%m != 0:
    pass
    else:
    x = 0
    if x == 1:
    templist.append(i)
    else:
    pass
    i = i + 1
    return templist

    mylist = factorize(var)
    print mylist
    time2 = time.clock()
    print 'time = ',time2-time1
