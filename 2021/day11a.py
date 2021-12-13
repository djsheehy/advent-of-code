grid = """8577245547
1654333653
5365633785
1333243226
4272385165
5688328432
3175634254
6775142227
6152721415
2678227325"""
grid = [[int(x) for x in row] for row in grid.split('\n')]
moves = [(-1, -1), ( 0, -1), (1, -1),
         (-1,  0),           (1,  0),
         (-1,  1), ( 0,  1), (1,  1)]

def step(grid):
    width = len(grid[0])
    height = len(grid)
    gonnaFlash = set()
    flashed = set()
    for row in range(height):
        for col in range(width):
            grid[row][col] += 1
            if grid[row][col] > 9:
                gonnaFlash.add((row, col))
                
    while gonnaFlash:
        row, col = gonnaFlash.pop()
        if (row, col) in flashed:
            continue
        for r, c in moves:
            nbr_row, nbr_col = row + r, col + c
            if nbr_row not in range(height) or nbr_col not in range(width):
                continue
            if (nbr_row, nbr_col) in flashed:
                continue
            grid[nbr_row][nbr_col] += 1
            if grid[nbr_row][nbr_col] > 9:
                gonnaFlash.add((nbr_row, nbr_col))
        grid[row][col] = 0
        flashed.add((row, col))
    return len(flashed)
                

def pg(grid):
    for row in grid:
        print(''.join(map(str, row)))

def main():
    score = 0
    for i in range(100):
        score += step(grid)

    print(score)

if __name__ == '__main__':
    main()