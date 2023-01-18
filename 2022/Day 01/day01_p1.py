with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")
m=0
s=0
for line in lines:#finding sum of calories and then taking maimum of it
    if len(line):
        s+=int(line)
    else:
        m=max(m,s)
        s=0
print(m)