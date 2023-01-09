with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

knots=[]
for i in range(10):#creating 10 knots
    knots.append([0,0])

visited=set()

def touching(x1,y1,x2,y2): # checking if they are touching or not
    return abs(x1-x2)<=1 and abs(y1-y2)<=1

def move(dx,dy):#moving all the knots one by one an adjusting the tails accordingly
    global knots
    knots[0][0]+=dx
    knots[0][1]+=dy
    for i in range(1,10):
        hx,hy=knots[i-1][0],knots[i-1][1]
        tx,ty=knots[i][0],knots[i][1]
        move_x,move_y=0,0
        if not touching(hx,hy,tx,ty):
            if hx != tx:
                move_x=(hx - tx) / abs(hx - tx)
            if hy != ty:
                move_y=(hy - ty) / abs(hy - ty)
            tx+=move_x
            ty+=move_y
        knots[i][0]=tx
        knots[i][1]=ty       

d={
    'L':[-1,0],
    'R':[1,0],
    'U':[0,1],
    'D':[0,-1]
}
for line in lines:
    visited.add((knots[9][0],knots[9][1]))
    dir,val=line.split()
    val=int(val)
    dx,dy=d[dir]
    for i in range(val):#moving one by one
        move(dx,dy)
        visited.add((knots[9][0],knots[9][1]))
print(len(visited))   