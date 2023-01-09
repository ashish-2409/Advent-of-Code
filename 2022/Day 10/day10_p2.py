with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

c=0
x=1
arr=[1]*241
for line in lines:
    l=line.split()
    if len(l)==1:#if instruction is noop
        c=c+1
        arr[c]=x
    else:# if instruction is add
        arr[c+1]=x
        v=int(l[1])
        c=c+2
        x+=v
        arr[c]=x

ans=[[None]*40 for _ in range(6)]
for i in range(6):
    for j in range(40):
        cn=i*40+j
        if abs(arr[cn]-j)<=1:
            ans[i][j]="#"
        else:
            ans[i][j]=" "
for i in range(6):
    print("".join(ans[i]))