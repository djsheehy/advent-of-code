gridnum = 5791

def power_level(x,y):
    rackID = x + 10
    power = rackID * y
    power += gridnum
    power *= rackID
    return (power / 100) % 10 - 5

best_cell = (0,0)
max_power = 0
for x in range(1, 299):
    for y in range(1, 299):
        p = 0
        for i in range(3):
            for j in range(3):
                p += power_level(x + i, y + j)
        if p > max_power:
            best_cell = (x, y)
            max_power = p

print(best_cell)