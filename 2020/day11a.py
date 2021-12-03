grid = open('input11.txt').readlines()
width = len(grid[0])
height = len(grid)

def step(grid):
    newgrid = [list(row) for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == '.':
                continue
            neighbors = 0
            for dr in [-1, 0, 1]:
                if (row + dr) not in range(height):
                    continue
                for dc in [-1, 0, 1]:
                    if (col + dc) not in range(width):
                        continue
                    if dr == 0 and dc == 0:
                        continue
                    if grid[row + dr][col + dc] == '#':
                        neighbors += 1
            if grid[row][col] == 'L' and neighbors == 0:
                newgrid[row][col] = '#'
            elif grid[row][col] == '#' and neighbors >= 4:
                newgrid[row][col] = 'L'
    return newgrid

newgrid = step(grid)
while newgrid != grid:
    grid = newgrid
    newgrid = step(grid)

answer = sum(row.count('#') for row in newgrid)
print(answer)