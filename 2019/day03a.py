f = open('input03.txt')
path1 = f.readline().strip()
path2 = f.readline().strip()
f.close()
path1 = path1.split(',')
path2 = path2.split(',')

def trace(path):
    x = 0
    y = 0
    ans = set()
    for move in path:
        d = move[0]
        l = int(move[1:])
        for i in range(l):
            if d == 'U':
                y -= 1
            elif d == 'D':
                y += 1
            elif d == 'L':
                x -= 1
            elif d == 'R':
                x += 1
            ans.add((x,y))
    if (0,0) in ans:
        ans.remove((0,0))
    return ans

wire1 = trace(path1)
wire2 = trace(path2)
cross = wire1.intersection(wire2)
answer = 100000000000
for x, y in cross:
    if (abs(x) + abs(y)) < answer:
        answer = abs(x) + abs(y)
print(answer)