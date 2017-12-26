f = open("input.txt")

lines = list(map(str.strip, f.readlines()))
f.close()
x = len(lines[0])//2
y = len(lines)//2
GRID = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        GRID[(j, i)] = c

class Virus:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
        self.dir = 0
        self.count = 0

    def move(self):
        "modify current cell and move"
        cell = self.grid.get((self.x, self.y), '.')
        if cell == ".":
            self.grid[(self.x, self.y)] = "W"
            self.dir = (self.dir-1) % 4
        elif cell == "W":
            self.grid[(self.x, self.y)] = "#"
            self.count += 1
        elif cell == "#":
            self.grid[(self.x, self.y)] = "F"
            self.dir = (self.dir+1) % 4
        elif cell == "F":
            self.grid[(self.x, self.y)] = "."
            self.dir = (self.dir+2) % 4
        if self.dir == 0:
            self.y -= 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        elif self.dir == 3:
            self.x -= 1

V = Virus(x, y, GRID)
for i in range(10000000):
    V.move()

print(V.count)
