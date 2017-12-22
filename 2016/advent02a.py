lines = open("input02.txt").read().strip().split('\n')
x,y = 1,1
def coord2digit(x,y):
    return y*3+x+1
moves = {'U':(0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0)}
ans = []

for l in lines:
    for cmd in l:
        m = moves[cmd]
        if (x+m[0]) in range(3) and (y+m[1]) in range(3):
            x, y = x+m[0], y+m[1]
    ans.append(coord2digit(x,y))

print(''.join(str(c) for c in ans))
