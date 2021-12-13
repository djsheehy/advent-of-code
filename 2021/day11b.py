from day11a import grid, step

ans = 1
flashes = step(grid)
while flashes < 100:
    flashes = step(grid)
    ans += 1
print(ans)