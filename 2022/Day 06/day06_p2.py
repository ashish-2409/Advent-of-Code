with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")

for line in lines:
    for i in range(len(line)):
        if len(set(line[i:i+14]))==14:#is all 14 characters are different then print and break
            print(i+14)
            break