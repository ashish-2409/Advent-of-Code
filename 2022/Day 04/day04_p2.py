with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")
ans = 0
for line in lines:
    # parsing input file
    l = line.split(',')
    a = l[0].split('-')
    b = l[1].split('-')
    l1 = int(a[0])
    r1 = int(a[1])
    l2 = int(b[0])
    r2 = int(b[1])
    # is the dont overlap then continue else add it to the answer
    if r1<l2 or r2<l1:
        continue
    ans+=1
print(ans)
