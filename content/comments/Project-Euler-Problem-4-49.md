post_id: Project-Euler-Problem-4
Author: progra
Date: 2010-07-20 19:29:51
Author_Email: noreply@blogger.com
Author_IP: None

// this is how i wrote the program the first time.<br /><br /><br />import java.util.*;<br />public class euler4 {<br /><br /> /**<br />  * @param args<br />  */<br /> public static void main(String[] args) {<br />  // TODO Auto-generated method stub<br />         int num1=999;<br />         int num2=999;<br />         int sum=0;<br />         int i=0;<br />         int [] arr=new int[6];<br />         int orig=0;<br />         int biggest=0;<br /> <br />         for(num1=999;num1>=100;num1--){<br />         for(num2=999;num2>=100;num2--){<br />             i=0;<br />          sum=num1*num2;<br />          orig=num1*num2;<br />            while(sum>0){<br />              arr[i]=sum%10;<br />                 sum=sum/10;<br />                  i++;<br />          }          <br />           if(arr[0]==arr[5]&&arr;[1]==arr[4]&&arr;[2]==arr[3]){<br />            if(biggest<orig><br />                biggest=orig;<br />            }<br />            } <br /> <br /> <br />           }<br />         }<br />         System.out.print(biggest);<br />         }<br /> }</orig>
