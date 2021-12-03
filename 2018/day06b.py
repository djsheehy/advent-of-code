f = open('input06.txt')
coords = [line.strip().split(', ') for line in f.readlines()]
coords = [tuple(int(x) for x in c) for c in coords]

minX = min(coords, key=lambda c: c[0])[0]
maxX = max(coords, key=lambda c: c[0])[0]
minY = min(coords, key=lambda c: c[1])[1]
maxY = max(coords, key=lambda c: c[1])[1]

def distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

result = 0
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        d = 0
        for c in coords:
            d += distance(x, y, c[0], c[1])
        if d < 10000:
            result += 1

print(result)