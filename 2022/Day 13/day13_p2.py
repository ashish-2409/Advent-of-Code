with open("input.txt") as fin:
    data=fin.read().strip()
    lines=data.split("\n")
def fun(p1,p2):
    if isinstance(p1, int) and isinstance(p2,int):# if both are int
        if p1<p2:
            return -1
        elif p1==p2:
            return 0
        else:
            return 1
    elif isinstance(p1, list) and isinstance(p2, list):# if both are lists
        i=0
        n1=len(p1)
        n2=len(p2)
        while i<n1 and i<n2:
            c=fun(p1[i], p2[i])#recursively go compare the list 
            if c==-1:
                return -1
            if c==1:
                return 1
            i += 1
        if i==n1 and i<n2:# if p1 is empty
            return -1
        elif i==n2 and i<n1:#if p2 is empty
            return 1
        else:# both are empty
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):# if one is int and the other is list, convert the int to list
        return fun([p1], p2)
    elif isinstance(p1, list) and isinstance(p2, int):
        return fun(p1, [p2])

l=[]
ans=0
for i,group in enumerate(data.split("\n\n")):
    p1,p2 = group.split('\n')
    p1 = eval(p1)
    p2 = eval(p2)
    l.append(p1)
    l.append(p2)
    if fun(p1, p2)==-1:#if in correct order add the index
        ans += 1+i

#adding the 2 divider packets
l.append([[2]])
l.append([[6]])
from functools import cmp_to_key
l = sorted(l, key=cmp_to_key(lambda p1,p2: fun(p1,p2)))# sorting them based on the function 
ans=[]
for i,p in enumerate(l):
    if p==[[2]] or p==[[6]]:# finding the index of [2] and [6] and stroing them in ans
        ans.append(i+1)
print(ans[0]*ans[1])# multipling the ans
