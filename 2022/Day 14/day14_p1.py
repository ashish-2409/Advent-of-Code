with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")
s=set()
for line in lines:
    all=[]
    l=line.split(" -> ")#getting all points
    for i in l:
        a=i.split(',')
        all.append([int(a[0]),int(a[1])])
    for i in range(1,len(all)):#creating horizontal and vertical lines from the adjacent points
        x1,y1=all[i]
        x2,y2=all[i-1]
        if y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                s.add((x1, y))
        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                s.add((x, y1))

# print(len(s))
# print(all)
# maxy=0
ans=0
maxy=max([i[1] for i in s])#getting the max y which is the limit to which sand can fall
# print(s)
# print(maxy)
def fun():#simulating each sand particle starting from 500,0 going down,left,right
    global s
    x,y=500,0
    while y<=maxy:
        if (x,y+1) not in s:
            y+=1
            continue
        if (x-1,y+1) not in s:
            y+=1
            x-=1
            continue        
        if (x+1,y+1) not in s:
            y+=1
            x+=1
            continue
        s.add((x,y))
        return True
    return False
ans=0
while True:
    x=fun()
    if not x:
        break
    ans+=1
print(ans)