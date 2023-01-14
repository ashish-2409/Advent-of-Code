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


l1 = []
l2 = []

for i, s in enumerate(sensor):
    d = dist[i]
    l2.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    l1.extend([s[0] - s[1] - d, s[0] - s[1] + d])


pos = None
neg = None

for i in range(2 * len(sensor)):
    for j in range(i + 1, 2 * len(sensor)):
        a, b = l1[i], l1[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = l2[i], l2[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1


x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4000000 + y
print(ans)
