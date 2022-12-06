import java.util.Collection;
import java.util.Scanner;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
class day1{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int m=0,c=0;
        Vector<Integer> v=new Vector<>();
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            if(s.length()==0){
                v.addElement(c);
                c=0;
            }
            else c+=Integer.parseInt(s);
        }
        Collections.sort(v);
        int s=0,i=v.size()-1;
        c=3;
        for(int j=0;j<3;j++){
            s+=v.elementAt(i);
            i--;
        }
        System.out.println(s);
    }
}