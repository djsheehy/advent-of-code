import re

f = open('input05.txt')
lines = []
for line in f:
    line = line.strip()
    m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    x1, y1, x2, y2 = [int(x) for x in m.groups()]
    lines.append([x1, y1, x2, y2])
f.close()

grid = {}

for x1, y1, x2, y2 in lines:
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for y in range(y1, y2+1):
            if (x1, y) in grid:
                grid[(x1, y)] += 1
            else:
                grid[(x1, y)] = 1
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        for x in range(x1, x2+1):
            if (x, y1) in grid:
                grid[(x, y1)] += 1
            else:
                grid[(x, y1)] = 1

    elif x1 < x2:
        if y1 < y2:
            # northwest to southeast
            for delta in range(x2 - x1 + 1):
                x = x1 + delta
                y = y1 + delta
                if (x, y) in grid:
                    grid[(x, y)] += 1
                else:
                    grid[(x, y)] = 1
        else:
            # sw to ne
            for delta in range(x2 - x1 + 1):
                x = x1 + delta
                y = y1 - delta
                if (x, y) in grid:
                    grid[(x, y)] += 1
                else:
                    grid[(x, y)] = 1
    else:
        if y1 < y2:
            # ne to sw
            for delta in range(y2 - y1 + 1):
                x = x1 - delta
                y = y1 + delta
                if (x, y) in grid:
                    grid[(x, y)] += 1
                else:
                    grid[(x, y)] = 1
        else:
            # se to nw
            for delta in range(y1 - y2 + 1):
                x = x1 - delta
                y = y1 - delta
                if (x, y) in grid:
                    grid[(x, y)] += 1
                else:
                    grid[(x, y)] = 1

answer = len([x for x in grid.values() if x > 1])
print(answer)