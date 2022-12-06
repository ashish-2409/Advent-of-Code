import java.util.Scanner;
import java.util.Set;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
class day4{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int ans=0;
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            String a[]=s.split(",");
            String ff[]=a[0].split("-");
            String ss[]=a[1].split("-");
            Boolean f=false;
            int l1=Integer.parseInt(ff[0]);
            int r1=Integer.parseInt(ff[1]);
            int l2=Integer.parseInt(ss[0]);
            int r2=Integer.parseInt(ss[1]);
            if(l2>=l1&&r2<=r1)f=true;
            if(l1>=l2&&r1<=r2)f=true;
            if(r1>=l2&&l1<=l2)f=true;
            if(r2>=l1&&l2<=l1)f=true;
            if(f)ans++;
        }
        System.out.println(ans);
    }
}