with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

c=1
x=1
ans=0
for line in lines:
    l=line.split()
    if len(l)==1:#if instruction is noop
        c=c+1
        if c==20 or c==60 or c==100 or c==140 or c==180 or c==220:
            ans+=x*c
    else:# if instruction is add
        v=int(l[1])
        c=c+1#first cycle of add
        if c==20 or c==60 or c==100 or c==140 or c==180 or c==220:
            ans+=x*c
        x+=v
        c+=1#second cycle of add
        if c==20 or c==60 or c==100 or c==140 or c==180 or c==220:
            ans+=x*c
print(ans)