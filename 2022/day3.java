import java.util.Scanner;
import java.util.Set;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
class day3{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int ans=0;
        HashMap<Character,Integer>m=new HashMap<>();
        int x=1;
        for(char c='a';c<='z';c++)m.put(c,x++);
        for(char c='A';c<='Z';c++)m.put(c,x++);
        while(sc.hasNextLine()){
            String a=sc.nextLine();
            String b=sc.nextLine();
            String c=sc.nextLine();
            Set<Character>s1=new HashSet<>();
            Set<Character>s2=new HashSet<>();
            Set<Character>s3=new HashSet<>();
            for(int i=0;i<a.length();i++){
                s1.add(a.charAt(i));
            }
            for(int i=0;i<b.length();i++){
                s2.add(b.charAt(i));
            }
            for(int i=0;i<c.length();i++){
                s3.add(c.charAt(i));
            }
            for(Character t:s1){
                if(s2.contains(t)&&s3.contains(t)){
                        ans+=(m.get(t));
                        // System.out.print(c+" ");
                }
            }
            // System.out.println();
        }
        System.out.println(ans);
    }
}