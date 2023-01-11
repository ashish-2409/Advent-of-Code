from heapq import heappop, heappush
with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")
l=[]
for line in lines:
    l.append(line)

# print(l)
n=len(l)
m=len(l[0])

for k in range(len(l)):
    for t in range(len(l[0])):
        if l[k][t]=='S':
            start=k,t
        if l[k][t]=='E':
            end=k,t
def val(c):#value of character
    if c=='S':
        return ord('a')
    if c=='E':
        return ord('z')
    return ord(c)

def adj(i, j):#adjacent characters
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if val(l[ii][jj]) <= val(l[i][j]) + 1:
            yield ii, jj

vis = []
for i in range(n):
    x=[]
    for j in range(m):
        x.append(False)
    vis.append(x)
hp = [(0, start[0], start[1])]

while True:#shortest path
    ans, i, j = heappop(hp)

    if vis[i][j]==True:
        continue
    vis[i][j] = True

    if (i, j) == end:
        print(ans)
        break

    for a, b in adj(i, j):
        heappush(hp, (ans + 1, a, b))