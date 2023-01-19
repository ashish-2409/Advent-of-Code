with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")

ans=0

for line in lines:
    a=line.split()
    if a[1]=='X':#score due to outcome or round
        ans+=0
    if a[1]=='Y':
        ans+=3
    if a[1]=='Z':
        ans+=6
    
    if a[0]=='A':#score due to shape choosen
        if a[1]=='Y':
            ans+=1
        if a[1]=='X':
            ans+=3
        if a[1]=='Z':
            ans+=2
    if a[0]=='B':
        if a[1]=='Z':
            ans+=3
        if a[1]=='Y':
            ans+=2
        if a[1]=='X':
            ans+=1
    if a[0]=='C':
        if a[1]=='X':
            ans+=2
        if a[1]=='Z':
            ans+=1
        if a[1]=='Y':
            ans+=3
print(ans)