import java.util.Scanner;
import java.util.Vector;

import javax.swing.plaf.synth.SynthOptionPaneUI;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
class day2{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int ans=0;
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            String a[]=s.split(" ");
            if(a[1].equals("X")){
                if(a[0].equals("A")){
                    ans+=3;
                }
                if(a[0].equals("B")){
                    ans++;
                }
                if(a[0].equals("C")){
                    ans+=2;
                }
            }
            if(a[1].equals("Y")){
                ans+=3;
                if(a[0].equals("A")){
                    ans++;
                }
                if(a[0].equals("B")){
                    ans+=2;
                }
                if(a[0].equals("C")){
                    ans+=3;
                }
            }
            if(a[1].equals("Z")){
                ans+=6;
                if(a[0].equals("A")){
                    ans+=2;
                }
                if(a[0].equals("B")){
                    ans+=3;
                }
                if(a[0].equals("C")){
                    ans++;
                }
            }
            
        }
        System.out.println(ans);
    }
}