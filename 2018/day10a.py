import re

f = open('input10.txt')
points = []

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def move(self, seconds):
        self.x += self.dx * seconds
        self.y += self.dy * seconds

for line in f:
    p = [int(x) for x in re.findall(r"-?\d+", line)]
    points.append(Point(*p))

def show_points(points):
    minx = min(map(lambda p: p.x, points))
    miny = min(map(lambda p: p.y, points))
    maxx = max(map(lambda p: p.x, points))
    maxy = max(map(lambda p: p.y, points))
    print(f'({maxx}, {maxy})')
    grid = []
    for i in range(maxy+1):
        grid.append(['.'] * (maxx + 1))
    for p in points:
        grid[p.y][p.x] = '#'
    for row in grid[miny:maxy+1]:
        print(''.join(row[minx:maxx+1]))

seconds = 0
while True:
    s = input("seconds: ")
    if s == 'p':
        show_points(points)
        continue
    try:
        s = int(s)
        seconds += s
        for p in points:
            p.move(s)
        minx = min(map(lambda p: p.x, points))
        miny = min(map(lambda p: p.y, points))
        maxx = max(map(lambda p: p.x, points))
        maxy = max(map(lambda p: p.y, points))
        print(f'{seconds} seconds')
        print(f'({minx}..{maxx}), ({miny}..{maxy})')
    except ValueError as e:
        pass