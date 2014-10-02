post_id: project-euler-problem-4
Author: progra
Date: 2010-07-20 19:29:51
Author_Email: noreply@blogger.com
Author_IP: None

    :::java
    // this is how i wrote the program the first time.


    import java.util.*;
    public class euler4 {

        /**
         * @param args
         */
        public static void main(String[] args) {
            // TODO Auto-generated method stub
            int num1=999;
            int num2=999;
            int sum=0;
            int i=0;
            int [] arr=new int[6];
            int orig=0;
            int biggest=0;

            for(num1=999;num1>=100;num1--){
                for(num2=999;num2>=100;num2--){
                    i=0;
                    sum=num1*num2;
                    orig=num1*num2;
                    while(sum>0){
                        arr[i]=sum%10;
                        sum=sum/10;
                        i++;
                    }
                    if(arr[0]==arr[5]&&arr;[1]==arr[4]&&arr;[2]==arr[3]){
                        if(biggest<orig)
                            biggest=orig;
                    }
                }

            }
            System.out.print(biggest);
        }
    }
