import java.util.Scanner;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
class day7{
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc=new Scanner(new File("input.txt"));
        HashMap<String,Integer>m=new HashMap<>();
        Vector<String>v=new Vector<>();
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            String a[]=s.split(" ");
            // System.out.println(s);
            if(a[0].equals("$")){
                if(a[1].equals("cd")){
                    if(a[2].equals("..")){
                        v.remove(v.size()-1);
                    }
                    else if(a[2].equals("/")){
                        v.removeAllElements();
                        v.add("/");
                    }
                    else{
                        v.add(a[2]);
                    }
                    if(v.size()==0)v.add("/");
                }
                // System.out.println(v+"\n");
            }
            else {
                try{
                    int x=Integer.parseInt(a[0]);
                    String t="";
                    for(int i=0;i<v.size();i++){
                        t+=v.elementAt(i);
                       Integer c=m.get(t);
                       if(c==null){
                            m.put(t,x);
                       }
                       else{
                            m.put(t,x+c);
                       }
                    }
                }
                catch(Exception e){

                }
            }
        }
        // System.out.println("\n");
        int ans=0;
        for(String i:m.keySet()){
            if(m.get(i)<=100000)ans+=m.get(i);
            // System.out.println(i+" "+m.get(i));
        }
        int to=m.get("/");
        int rem=70000000-to;
        int req=30000000-rem;
        ans=70000000;
        for(Integer i:m.values()){
            if(i>=req){
                ans=Math.min(ans,i);
            }
        }
        System.out.println(ans);
    }
}