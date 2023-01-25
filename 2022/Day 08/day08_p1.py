with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")

ans=0
l=[]#stroing the grid
for line in lines:
    l.append(line)

n=len(l)
m=len(l[0])
# print(l)
for i in range(n):
    for j in range(m):
        a=b=c=d=1
        #checkign all directions to see if any one is valid
        for k in range(0,i):
            if l[k][j]>=l[i][j]:
                a=0
                break
        for k in range(i+1,n):
            if l[k][j]>=l[i][j]:
                b=0
                break
        for k in range(0,j):
            if l[i][k]>=l[i][j]:
                c=0
                break
        for k in range(j+1,m):
            if l[i][k]>=l[i][j]:
                d=0
                break
        ans+= (a or b or c or d)
print(ans)            