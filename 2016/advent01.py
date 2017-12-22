f = open("input01.txt")
data = f.read().split(", ")
x,y = 0,0
dir = 0
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
visited = set()
ans = 0
for move in data:
    if move[0] == 'L':
        dir = (dir-1) % 4
    else:
        dir = (dir+1) % 4
    dist = int(move[1:])
    dxy = dirs[dir]
    for i in range(dist):
        x += dxy[0]
        y += dxy[1]
        if not ans:
            if (x,y) in visited:
                ans = abs(x)+abs(y)
            else:
                visited.add((x,y))

print(abs(x)+abs(y))
print(ans)
