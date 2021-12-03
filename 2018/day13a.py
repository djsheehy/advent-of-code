f = open('input13.txt')
tracks = [l.strip() for l in f]
f.close()

turns = {'^': '<>^', '>': '^V>', 'V': '><V', '<': 'V^<'}
moves = {'^': (0, -1), '>': (1, 0), 'V': (0, -1), '<': (-1, 0)}
curve = {'/': {'^': '>', '>': '^', 'V': '<', '<': 'V'},
         '\\':{'^': '<', '>': 'V', 'V': '>', '<': '^'}}

class Cart:
    def __init__(self, tracks, x, y, direction):
        self.tracks = tracks
        self.x = x
        self.y = y
        self.dir = direction
        self.turn = 0
    
    def move(self):
        print(f"Moving cart at {(self.x, self.y)}")
        c = self.tracks[self.y][self.x]
        # move forward
        dx, dy = moves[self.dir]
        self.x += dx
        self.y += dy
        
        # decide how to turn
        if c in '/\\':
            self.dir = curve[c][self.dir]
        elif c == '+':
            self.dir = turns[self.dir][self.turn]
            self.turn = (self.turn + 1) % 3

# scan for carts
carts = []
for y, row in enumerate(tracks):
    for x, c in enumerate(row):
        if c in '<>^V':
            print(f"Found cart at {(x, y)}")
            carts.append(Cart(tracks, x, y, c))

# clean up the map
tracks = [row.replace('^', '|').replace('V', '|').replace('<', '-').replace('>', '-') for row in tracks]

def moveCarts():
    carts.sort(key=lambda c: (c.y, c.x))
    coords = set()
    for c in carts:
        c.move()
        if (c.x, c.y) in coords:
            return (c.x, c.y)
        coords.add((c.x, c.y))

answer = None
while not answer:
    answer = moveCarts()
print(answer)
