f = open("input.txt")
grid = {}
for i, line in enumerate(f):
    for j, c in enumerate(line):
        grid[(j, i)] = c

x, y = (12, 12)
d = 0
count = 0

for i in range(10000):
    if (x,y) in grid and grid[(x,y)] == '#':
        d = (d+1) % 4
        grid[(x,y)] = '.'
    else:
        d = (d-1) % 4
        grid[(x,y)] = '#'
        count += 1
    
    if d == 0:
        y -= 1
    elif d == 1:
        x += 1
    elif d == 2:
        y += 1
    elif d == 3:
        x -= 1

print(count)