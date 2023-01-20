with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")
ans=0
a=''
b=''
c=''
for line in lines:
    if a=="":
        a=line
        continue
    if b=="":
        b=line
        continue
    if c=="":
        c=line
        continue
    s=set(a)&set(b)&set(c)
    x=0
    # print(a,b,c)
    for i in s:
        # print(i)
        if i>='a' and i<='z':
            ans+=ord(i)-ord('a')+1
        if i>='A' and i<='Z':
            ans+=ord(i)-ord('A')+1+26
    a=line
    b=c=""
s=set(a)&set(b)&set(c)
for i in s:
    # print(i)
    if i>='a' and i<='z':
        ans+=ord(i)-ord('a')+1
    if i>='A' and i<='Z':
        ans+=ord(i)-ord('A')+1+26
# print(a,b,c)
print(ans)