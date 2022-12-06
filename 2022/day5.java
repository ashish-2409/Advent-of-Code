import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
class day5{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        int ans=0;
        Vector<Vector<Character>> v =new Vector<>();
        // String s="ABCD";
        for(int i=0;i<9;i++)v.add(new Vector<Character>());
        v.elementAt(0).addElement('D');
        v.elementAt(0).addElement('L');
        v.elementAt(0).addElement('V');
        v.elementAt(0).addElement('T');
        v.elementAt(0).addElement('M');
        v.elementAt(0).addElement('H');
        v.elementAt(0).addElement('F');
        
        v.elementAt(1).addElement('H');
        v.elementAt(1).addElement('Q');
        v.elementAt(1).addElement('G');
        v.elementAt(1).addElement('J');
        v.elementAt(1).addElement('C');
        v.elementAt(1).addElement('T');
        v.elementAt(1).addElement('N');
        v.elementAt(1).addElement('P');

        v.elementAt(2).addElement('R');
        v.elementAt(2).addElement('S');
        v.elementAt(2).addElement('D');
        v.elementAt(2).addElement('M');
        v.elementAt(2).addElement('P');
        v.elementAt(2).addElement('H');

        v.elementAt(3).addElement('L');
        v.elementAt(3).addElement('B');
        v.elementAt(3).addElement('V');
        v.elementAt(3).addElement('F');

        v.elementAt(4).addElement('N');
        v.elementAt(4).addElement('H');
        v.elementAt(4).addElement('G');
        v.elementAt(4).addElement('L');
        v.elementAt(4).addElement('Q');

        v.elementAt(5).addElement('W');
        v.elementAt(5).addElement('B');
        v.elementAt(5).addElement('D');
        v.elementAt(5).addElement('G');
        v.elementAt(5).addElement('R');
        v.elementAt(5).addElement('M');
        v.elementAt(5).addElement('P');

        v.elementAt(6).addElement('G');
        v.elementAt(6).addElement('M');
        v.elementAt(6).addElement('N');
        v.elementAt(6).addElement('R');
        v.elementAt(6).addElement('C');
        v.elementAt(6).addElement('H');
        v.elementAt(6).addElement('L');
        v.elementAt(6).addElement('Q');

        v.elementAt(7).addElement('C');
        v.elementAt(7).addElement('L');
        v.elementAt(7).addElement('W');

        v.elementAt(8).addElement('R');
        v.elementAt(8).addElement('D');
        v.elementAt(8).addElement('L');
        v.elementAt(8).addElement('Q');
        v.elementAt(8).addElement('J');
        v.elementAt(8).addElement('Z');
        v.elementAt(8).addElement('M');
        v.elementAt(8).addElement('T');

        
        
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            s=s.trim();
            String a[]=s.split(" ");
            try{
                int x=Integer.parseInt(a[a.length-1]);
                break;
            }
            catch(Exception e){
            }
        }
        sc.nextLine();
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            String a[]=s.split(" ");
            int c=Integer.parseInt(a[1]);
            int st=Integer.parseInt(a[3])-1;
            int en=Integer.parseInt(a[5])-1;
            Vector<Character>t=new Vector<>();
            while(c>0){
                t.addElement(v.elementAt(st).lastElement());
                v.elementAt(st).remove(v.elementAt(st).size()-1);
                c--;
            }
            for(int i=t.size()-1;i>=0;i--){
                v.elementAt(en).addElement(t.elementAt(i));
            }
        } 
        String as="";
        for(int i=0;i<9;i++){
            as+=v.elementAt(i).lastElement();
        }
        System.out.println(as);
    }
}