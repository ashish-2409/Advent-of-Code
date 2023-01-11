from heapq import heappop, heappush

with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

l = []
for line in lines:
    l.append(line)
n = len(l)
m = len(l[0])

for i in range(n):
    for j in range(m):
        char = l[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j


def val(s):
    if s == "S":
        return ord('a')
    if s == "E":
        return ord('z')
    return ord(s)


def adj(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if val(l[ii][jj]) >= val(l[i][j]) - 1:
            yield ii, jj
vis = []
for i in range(n):
    x=[]
    for j in range(m):
        x.append(False)
    vis.append(x)
hp = [(0, end[0], end[1])]
#we have to find shortest distance from any 'a' to 'E'
#here we i am finding shortest distance from 'E' to the nearest 'a'( reverse of the problem)
# as now we have 1 starting ponit instead of multiple 
while True:
    ans, i, j = heappop(hp)
    if vis[i][j]:
        continue
    vis[i][j] = True
    if val(l[i][j]) == ord('a'):
        print(ans)
        break
    for ii, jj in adj(i, j):
        heappush(hp, (ans + 1, ii, jj))