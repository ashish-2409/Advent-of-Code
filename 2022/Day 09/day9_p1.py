with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

tx,ty,hx,hy=0,0,0,0 #setting up x and y for head and tail
visited=set()

def touching(x1,y1,x2,y2): # checking if they are touching or not
    return abs(x1-x2)<=1 and abs(y1-y2)<=1

def move(dx,dy):#moving head by dx and dy and then depending upon the position of tail moving tail by atmost 1 
    global hx,hy,tx,ty
    hx+=dx
    hy+=dy
    move_x,move_y=0,0
    if not touching(hx,hy,tx,ty):
        if hx != tx:
            move_x=(hx - tx) / abs(hx - tx)
        if hy != ty:
            move_y=(hy - ty) / abs(hy - ty)
    tx+=move_x
    ty+=move_y       

d={
    'L':[-1,0],
    'R':[1,0],
    'U':[0,1],
    'D':[0,-1]
}
for line in lines:
    visited.add((tx,ty))
    dir,val=line.split()
    val=int(val)
    dx,dy=d[dir]
    for i in range(val):#moving one by one
        move(dx,dy)
        visited.add((tx,ty))#adding to the visited squares
print(len(visited))   