from math import atan2

f = open('input10.txt')
data = [l.strip() for l in f]
f.close()

asteroids = []
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == '#':
            asteroids.append((x,y))

def scan_rocks():
    for x,y in asteroids:
        angles = set()
        for x2, y2 in asteroids:
            if (x, y) == (x2, y2):
                continue
            angles.add(atan2(x2-x, y2-y))
        yield (x,y,len(angles))

x, y, count = max(scan_rocks(), key=lambda a: a[2])
print(f"Best is {(x, y)} with {count} other asteroids detected")