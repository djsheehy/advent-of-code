grid = [l.strip() for l in open('input03.txt').readlines()]
width = len(grid[0])
height = len(grid)

def slope(right, down):
    ans = 0
    x = 0
    y = 0
    while y < height:
        if grid[y][x % width] == '#':
            ans += 1
        x += right
        y += down
    return ans

answer = 1
for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    answer *= slope(right, down)
print(answer)