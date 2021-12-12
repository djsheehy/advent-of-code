data = [[int(n) for n in row.strip()] for row in open('input09.txt')]
width = len(data[0])
height = len(data)

from itertools import product

def lowPoint(coords):
    row, col = coords
    n = data[row][col]
    if n == 9:
        return False
    if row - 1 > 0 and n >= data[row-1][col]:
        return False
    if row + 1 < height and n >= data[row+1][col]:
        return False
    if col - 1 > 0 and n >= data[row][col-1]:
        return False
    if col + 1 < width and n >= data[row][col+1]:
        return False
    return True

def neighbors(point):
    row, col = point
    return {(row + r, col + c) for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)] 
            if (row + r) in range(height) and (col + c) in range(width) and data[row+r][col+c] != 9}
    

def basinSize(point):
    q = [point]
    visited = set()
    while q:
        node = q.pop()
        visited.add(node)
        q.extend(neighbors(node) - visited)
    return len(visited)
    

points = filter(lowPoint, product(range(height), range(width)))
basins = sorted(map(basinSize, points), reverse=True)
print(basins[0] * basins[1] * basins[2])