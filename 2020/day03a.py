grid = [l.strip() for l in open('input03.txt').readlines()]
width = len(grid[0])
height = len(grid)
answer = 0
for y in range(height):
    if grid[y][(y * 3) % width] == '#':
        answer += 1
print(answer)