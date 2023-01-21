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
    # checking if one range is contained in the other
    if l1 >= l2 and r1 <= r2:
        ans += 1
    elif l1 <= l2 and r1 >= r2:
        ans += 1
print(ans)
