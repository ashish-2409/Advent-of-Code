with open("input.txt") as fin:#reading file
    lines = fin.read().strip().split("\n")
l=[]
s=0
for line in lines:#finding sum of calories and then taking maimum of it
    if len(line):
        s+=int(line)
    else:
        l.append(s)
        s=0
l.sort()#sorting all calories
print(l[-1]+l[-2]+l[-3])#printing the sum of top 3 elves with maximum calories