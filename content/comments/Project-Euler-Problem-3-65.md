post_id: Project-Euler-Problem-3
Author: lolpium
Date: 2010-10-18 18:10:17
Author_Email: noreply@blogger.com
Author_IP: None

Hey I&#39;m very much a beginner but was pretty stoked I could run this in 3164ms. Heres the code --<br /><br />#The prime factors of 13195 are 5, 7, 13 and 29.<br />#What is the largest prime factor of the number 600851475143?<br />import os, sys, math, sets, time<br /><br />time1 = time.clock()<br />iniList = []<br /><br />var = 600851475143<br /><br />def factorize(num):<br />    templist = []<br />    max = int(math.sqrt(num))<br />    print &quot;max = &quot;,max<br />    i = 1<br />    while i m and i%m != 0:<br />                        pass<br />                    else:<br />                        x = 0<br />                if x == 1:<br />                    templist.append(i)    <br />        else:<br />            pass<br />        i = i + 1<br />    return templist<br /><br />mylist = factorize(var)<br />print mylist<br />time2 = time.clock()<br />print &#39;time = &#39;,time2-time1
