with open("input.txt") as fin: # reading file
    lines = fin.read().strip().split("\n")
    l = list(enumerate(map(int, lines)))

n = len(l)
og = l.copy()
def swap(l, a, b):#swapping
    l[a], l[b] = l[b], l[a]
    return l

for i, x in og:#going over all elements
    for idx in range(n):
        if l[idx][0] == i:
            break
    if x < 0:
        c = idx
        for _ in range(-x):
            l = swap(l, c, (c - 1) % n)
            c = (c - 1) % n
    elif  x > 0:
        c = idx
        for _ in range(x):
            l = swap(l, c, (c + 1) % n)
            c = (c + 1) % n

for j in range(n):
    if l[j][1] == 0:
        break
ans=l[(j + 1000) % n][1]+l[(j + 2000) % n][1]+l[(j + 3000) % n][1]
print(ans)