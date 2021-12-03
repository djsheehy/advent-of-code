import re

r = re.compile(r"<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>")
f=open('input12.txt')
moons = []

class Moon:
    def __init__(self, coords):
        self.coords = coords
        self.velocity = [0,0,0]
    
    def gravity(self, other):
        for i in range(3):
            if self.coords[i] < other.coords[i]:
                self.velocity[i] += 1
                other.velocity[i] -= 1
            elif self.coords[i] > other.coords[i]:
                self.velocity[i] -= 1
                other.velocity[i] += 1
    
    def move(self):
        for i in range(3):
            self.coords[i] += self.velocity[i]
    
    def energy(self):
        potential = sum(abs(c) for c in self.coords)
        kinetic = sum(abs(v) for v in self.velocity)
        return potential * kinetic

for line in f:
    line = line.strip()
    m = r.match(line)
    coords = [int(m[1]), int(m[2]), int(m[3])]
    moons.append(Moon(coords))

for i in range(1000):
    for a in range(3):
        for b in range(a, 4):
            moons[a].gravity(moons[b])
    for m in moons:
        m.move()

e = [m.energy() for m in moons]
print(sum(e))