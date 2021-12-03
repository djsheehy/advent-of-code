f = open('input03.txt')
path1 = f.readline().strip()
path2 = f.readline().strip()
f.close()
path1 = path1.split(',')
path2 = path2.split(',')

def trace(path):
    x, y, steps = 0,0,0
    ans = {}
    for move in path:
        d = move[0]
        l = int(move[1:])
        for i in range(l):
            steps += 1
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'L':
                x -= 1
            elif d == 'R':
                x += 1
            if (x,y) not in ans:
                ans[(x,y)] = steps
    return ans

wire1 = trace(path1)
wire2 = trace(path2)
cross = set(wire1.keys()).intersection(wire2.keys())
cross_steps = dict([c, wire1[c]+wire2[c]] for c in cross)
closest = min(cross, key=lambda k: cross_steps[k])
print(cross_steps[closest])