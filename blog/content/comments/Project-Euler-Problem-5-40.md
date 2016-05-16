post_id: project-euler-problem-5
Author: progra
Date: 2010-07-20 23:08:07
Author_Email: noreply@blogger.com
Author_IP: None

my java solution

    :::java
    import java.util.*;
    public class euler5 {

     /**
      * @param args
      */
     public static void main(String[] args) {
      // TODO Auto-generated method stub
             int i=2520;
             int j=0;
          boolean check=false;

          while(check==false){
           for(j=3;j<=20;j++){
            if(i%j!=0){
             check=false;
             j=21;
            }
            else{
             check=true;
            }

           }
           i=i+20;
          }
           System.out.println(i-20);
     }

    }
