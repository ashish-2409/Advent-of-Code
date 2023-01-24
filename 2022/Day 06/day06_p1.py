with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")

for line in lines:
    for i in range(len(line)):
        if len(set(line[i:i+4]))==4:#is all 4 characters are different then print and break
            print(i+4)
            break