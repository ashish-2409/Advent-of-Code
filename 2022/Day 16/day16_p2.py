from collections import deque
with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

valves={}
tunnels={}
nonempty=[]

for line in lines:#parsing the input
    x=line.split(";")
    a=x[0].split('=')
    val=int(a[1])
    a=a[0].split()
    point=a[1]
    valves[point]=val
    a=x[1].split(',')
    l=[]
    for i in a:
        l.append(i[len(i)-2:])
    tunnels[point]=l

# print(valves)
# print(tunnels)

dists = {}
nonempty = []

for valve in valves:#getting distance between each pair
    if valve != "AA" and not valves[valve]:
        continue
    
    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}
    
    queue = deque([(0, valve)])
    
    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}#memorization

def dfs(time, valve, bitmask):#dfs over all states
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)
        
    cache[(time, valve, bitmask)] = maxval
    return maxval

# print(dfs(30, "AA", 0))

#going through all possible partitions of valves and giving one set to us and the other to elephant
b=(1<<len(nonempty))-1
ans=0
for i in range((b+1)):
    ans=max(ans,dfs(26,'AA',i)+dfs(26,'AA',i^b))

print(ans)