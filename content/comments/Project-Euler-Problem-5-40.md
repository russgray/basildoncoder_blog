post_id: Project-Euler-Problem-5
Author: progra
Date: 2010-07-20 23:08:07
Author_Email: noreply@blogger.com
Author_IP: None

my java solution<br /><br />import java.util.*;<br />public class euler5 {<br /><br /> /**<br />  * @param args<br />  */<br /> public static void main(String[] args) {<br />  // TODO Auto-generated method stub<br />         int i=2520;<br />         int j=0;<br />      boolean check=false;<br /> <br />      while(check==false){<br />       for(j=3;j<=20;j++){<br />        if(i%j!=0){<br />         check=false;<br />         j=21;<br />        }<br />        else{<br />         check=true;<br />        }<br /> <br />       }<br />       i=i+20;<br />      }<br />       System.out.println(i-20);<br /> }<br /><br />}
