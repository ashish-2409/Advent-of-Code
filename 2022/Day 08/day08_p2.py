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
        a=b=c=d=0
        #checking all directions to see the farthest distance and then getting the scenic score
        for k in range(i-1,-1,-1):
            if l[k][j]>=l[i][j]:
                a+=1
                break
            else:
                a+=1
        for k in range(i+1,n):
            if l[k][j]>=l[i][j]:
                b+=1
                break
            else:
                b+=1
        for k in range(j-1,-1,-1):
            if l[i][k]>=l[i][j]:
                c+=1
                break
            else:
                c+=1
        for k in range(j+1,m):
            if l[i][k]>=l[i][j]:
                d+=1
                break
            else:
                d+=1
        # print(i,j)
        # print(a,b,c,d)
        ans=max(ans,a*b*c*d)
print(ans)            