with open("input.txt") as fin:  # reading file
    lines = fin.read().strip().split("\n")
l = []
val ="DLVTMHF,HQGJCTNP,RSDMPH,LBVF,NHGLQ,WBDGRMP,GMNRCHLQ,CLW,RDLQJZMT"#hard coding the stacks
val=val.split(',')
for i in val:
    l.append(list(i))
# print(len(l))
for line in lines:
    x=line.split()
    st=int(x[3])-1
    en=int(x[5])-1
    cn=int(x[1])
    while cn>0:#simulating the transfer of crates
        cn-=1
        l[en].append(l[st][-1])
        l[st].pop(len(l[st])-1)
for i in l:
    print(i[-1],end="")