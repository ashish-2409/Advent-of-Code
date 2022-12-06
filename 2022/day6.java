import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
class day6{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int ans=-1;
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            for(int i=0;i<=s.length()-14;i++){
                Set<Character> st=new HashSet();
                for(int j=0;j<14;j++)st.add(s.charAt(i+j));
                if(st.size()==14){
                    ans=i+14;break;
                }
            }
        }
        System.out.println(ans);
        
    }
}