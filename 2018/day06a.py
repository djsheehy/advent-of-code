f = open('input06.txt')
coords = [line.strip().split(', ') for line in f.readlines()]
coords = [tuple(int(x) for x in c) for c in coords]

minX = min(coords, key=lambda c: c[0])[0]
maxX = max(coords, key=lambda c: c[0])[0]
minY = min(coords, key=lambda c: c[1])[1]
maxY = max(coords, key=lambda c: c[1])[1]

def distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

grid = {}
# For each square on the grid, record the closest point
for x in range(minX, maxX + 1):
    for y in range(minY, maxY + 1):
        dist = [[c, distance(x, y, c[0], c[1])] for c in coords]
        dist.sort(key=lambda x: x[1])
        # if there's a tie, set it to None
        if dist[0][1] == dist[1][1]:
            grid[(x, y)] = None
        else:
            grid[(x, y)] = dist[0][0]

# if a point is closest to the boundary, its area is infinite
infinite = set()
# check top and bottom edge
for x in range(minX, maxX + 1):
    if grid[(x, minY)] is not None:
        infinite.add(grid[(x, minY)])
    if grid[(x, maxY)] is not None:
        infinite.add(grid[(x, maxY)])
# check left and right edge
for y in range(minY, maxY + 1):
    if grid[(minX, y)] is not None:
        infinite.add(grid[(minX, y)])
    if grid[(maxX, y)] is not None:
        infinite.add(grid[(maxX, y)])

area = dict((c, 0) for c in coords if c not in infinite)
for v in grid.values():
    if v in area:
        area[v] += 1

print(max(area.values()))