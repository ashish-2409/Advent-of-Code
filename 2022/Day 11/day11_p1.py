with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

ans=[0]*10
l=[]
test=[]
check=[]
exp=[]
ind=0
for line in lines:#adding all the data case by case using multiple conditions
    line=line.strip()
    if(line.startswith("Monkey")):
        ind=int(line[len(line)-2])
    if(line.startswith("Starting")):
        t=line.split(':')
        t=t[1].strip()
        t=t.split(',')
        x=[]
        for i in t:
            e=i.strip()
            x.append(int(e))
        l.append(x)
    if line.startswith("Test"):
        x=line.split()
        x=int(x[-1])
        test.append(x)
    if line.startswith("If"):
        x=line.split()
        if x[1]=="true:":
            t=[int(x[-1])]
            check.append(t)
        if x[1]=="false:":
            check[-1].append(int(x[-1]))
    if line.startswith("Operation"):
        x=line.split('=')
        x=x[1]
        y=x.replace("old","x")
        exp.append(y)

n=len(test)
for r in range(20):#over all rounds till 20 and simulating the algo for each monkey and each item
    for i in range(n):
        for j in l[i]:
            # print(l[i])
            x=j
            # print(x)
            y=eval(exp[i])
            y=y//3
            # y=round(y)
            # print(y)
            if y%test[i]==0:
                l[check[i][0]].append(y)
            else:
                l[check[i][1]].append(y)
            # l[i].pop(0)            
            ans[i]+=1
        l[i]=[]
        # print()
    # print(l)
# print(ans)
ans.sort()
print(ans[-1]*ans[-2])