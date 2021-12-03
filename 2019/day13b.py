from vm import Machine

def display(grid):
    for row in grid:
        s = ''.join(' #$_o'[tile] for tile in row)
        print(s)

f = open('input13.txt')
code = [int(c) for c in f.read().strip().split(',')]
f.close()
code[0] = 2
m = Machine(code)
m.input = 1
grid = [[0 for i in range(44)] for j in range(24)]
score = 0
ballX = 0
ballY = 0
while m.running:
    x = m.run()
    y = m.run()
    tile = m.run()
    if (x,y) == (-1,0):
        score = tile
        print(f"score = {score}")
    else:
        grid[y][x] = tile
        print(f"tile {(x,y)} = {tile}")
        if tile == 4:
            ballX = x
            ballY = y
            print((ballX, ballY))
    