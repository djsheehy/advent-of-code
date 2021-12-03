grid = [line.strip() for line in open('input11.txt').readlines()]
width = len(grid[0])
height = len(grid)

neighbors = [[[] for c in range(width)] for r in range(height)]
directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
for row in range(height):
    for col in range(width):
        if grid[row][col] == '.':
            continue
        for (dr, dc) in directions:
            r = row + dr
            c = col + dc
            while r in range(height) and c in range(width):
                if grid[r][c] != '.':
                    neighbors[row][col].append((r, c))
                    break
                r += dr
                c += dc

def step(grid):
    newgrid = [list(row) for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == '.':
                continue
            occupied = 0
            for r, c in neighbors[row][col]:
                if grid[r][c] == '#':
                    occupied += 1
            if grid[row][col] == 'L' and occupied == 0:
                newgrid[row][col] = '#'
            elif occupied >= 5:
                newgrid[row][col] = 'L'
    return newgrid

newgrid = step(grid)
while grid != newgrid:
    grid = newgrid
    newgrid = step(grid)

answer = sum(row.count('#') for row in newgrid)
print(answer)