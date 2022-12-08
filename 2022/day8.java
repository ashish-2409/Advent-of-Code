import java.util.Scanner;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
class day8{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        Vector<String>v=new Vector<>();
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            v.add(s);
        }
        int ans=0;
        int n=v.size(),m=v.elementAt(0).length();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                char c=v.elementAt(i).charAt(j);
                int c1=0,c2=0,c3=0,c4=0;
                
                
                for(int k=j-1;k>=0;k--){
                    c1++;
                    if(v.elementAt(i).charAt(k)>=c){
                        break;
                    }
                }
                for(int k=j+1;k<m;k++){
                    c2++;
                    if(v.elementAt(i).charAt(k)>=c){
                        break;
                    }
                }
                for(int k=i-1;k>=0;k--){
                    c3++;
                    if(v.elementAt(k).charAt(j)>=c){
                        break;
                    }
                }
                
                for(int k=i+1;k<n;k++){
                    c4++;
                    if(v.elementAt(k).charAt(j)>=c){
                        break;
                    }
                }
                ans=Math.max(ans, (c1*c2*c3*c4));
            }
        }
        System.out.println(ans);
    }
}