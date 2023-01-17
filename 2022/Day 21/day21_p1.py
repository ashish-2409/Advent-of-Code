from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")


lookup = {}#for storing expressions

def compute(name):#recursively calculating the value of each monkey
    if isinstance(lookup[name], int):
        return lookup[name]

    parts = lookup[name]
    left = compute(parts[0])
    right = compute(parts[2])

    x=parse_expr(f"({left}){parts[1]}({right})")#evaluating expresseion
    # print(name,parts,f"({left}){parts[1]}({right})",x)
    return x


for line in lines:#creaating the lookup table
    parts = line.split(" ")

    monkey = parts[0][:-1]

    if len(parts) == 2:
        lookup[monkey] = int(parts[1])
    else:
        lookup[monkey] = parts[1:]


left = compute(lookup["root"][0])
right = compute(lookup["root"][2])

ans = solve_linear(left, right)[1]
# print(left,right)
parts = lookup["root"]
ans=parse_expr(f"({left}){parts[1]}({right})")
# print((lookup["root"]))
print(ans)#answer for 'root'monkey