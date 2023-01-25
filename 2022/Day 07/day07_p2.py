with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")
l=['/']
d={}
for line in lines:
    x=line.split()
    # print(x)
    #using if conditions to get perform the required operation 
    if x[0]=='$':
        if x[1]=='cd':
            if x[2]=='..':
                l.pop(-1)
            elif x[2]=='/':
                l.clear()
                l.append('/')
            else:
                l.append(x[2]+'/')
        elif x[1]=='ls':
            continue
    else:
        try:
            size=int(x[0])
            path=""
            for i in l:#adding file size to all the parent directories as well
                path+=i
                if path in d:
                    d[path]+=size
                else:
                    d[path]=size
            # print(path,size)
        except:
            continue
ans=70000000
req=30000000
curr=70000000-d['/']
req=req-curr
#req is the minimum additional space we need to clear
for i in d:#calculating answer
    # print(i,d[i])
    if d[i]>=req:
        ans=min(ans,d[i])
print(ans)