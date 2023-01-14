with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")
def fun(a, b):#returns the manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
sensor =[]
beacon =[]
for line in lines:#parsing the input
    x=line.split(':')
    a=x[0].split()
    # sensor 
    x=a[-2].strip()
    x=int(x[:len(x)-1].split('=')[1])
    y=int(a[-1].strip().split('=')[1])
    sensor.append((x,y))
    #beacon
    x=line.split(':')
    a=x[1].split()
    x=a[-2].strip()
    x=int(x[:len(x)-1].split('=')[1])
    y=int(a[-1].strip().split('=')[1])
    beacon.append((x,y))

dist = []

for i in range(len(sensor)):#getting distance b/w all sensor and beaxon pairs
    dist.append(fun(sensor[i], beacon[i]))

val = 2000000
all = []

for i, s in enumerate(sensor):#getting all answer intervals
    dx = dist[i] - abs(s[1] - val)
    if dx <= 0:
        continue
    all.append((s[0] - dx, s[0] + dx))
# print(all)

excluded = []
for bx, by in beacon:#all beacons which lie on the val line
    if by == val:
        excluded.append(bx)


minx = min([i[0] for i in all])
maxx = max([i[1] for i in all])
ans = 0
for i in range(minx, maxx + 1):#checking all the points whether they lie in the interval and are not beacon
    if i in excluded:
        continue
    for left, right in all:
        if left <= i <= right:
            ans += 1
            break
print(ans)