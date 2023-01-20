with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")
ans=0
for line in lines:
    n=len(line)
    a=line[:n//2]#dividing into 2 compartments
    b=line[n//2:]
    a=set(a)
    b=set(b)
    c=a&b
    for i in c:
        if i>='a' and i<='z':
            ans+=ord(i)-ord('a')+1
        if i>='A' and i<='Z':
            ans+=ord(i)-ord('A')+1+26
print(ans)