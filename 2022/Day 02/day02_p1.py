with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")

ans=0

for line in lines:
    a=line.split()
    ans+=ord(a[1])-ord('X')+1#score for what we choose
    if a[0]=='A':#score fot the outcome of the round
        if a[1]=='Y':
            ans+=6
        if a[1]=='X':
            ans+=3
    if a[0]=='B':
        if a[1]=='Z':
            ans+=6
        if a[1]=='Y':
            ans+=3
    if a[0]=='C':
        if a[1]=='X':
            ans+=6
        if a[1]=='Z':
            ans+=3
print(ans)