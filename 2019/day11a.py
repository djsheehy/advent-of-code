from collections import defaultdict

POSITIION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

f = open('input11.txt')
code = [int(c) for c in f.read().strip().split(',')]
f.close()

def decode(n):
    "Decode an opcode"
    opcode = n % 100
    mode1 = (n // 100) % 10
    mode2 = (n // 1000) % 10
    mode3 = (n // 10000) % 10
    return (opcode, mode1, mode2, mode3)

class Machine:
    def __init__(self, code):
        self.memory = defaultdict(int, enumerate(code))
        self.pc = 0
        self.rbase = 0
        self.input = 0
        self.running = True
    
    def getParams(self):
        opcode, mode1, mode2, mode3 = decode(self.memory[self.pc])
        a = self.memory[self.pc+1]
        b = self.memory[self.pc+2]
        c = self.memory[self.pc+3]
        if mode1 == POSITIION_MODE:
            a = self.memory[a]
        elif mode1 == RELATIVE_MODE:
            a = self.memory[a + self.rbase]
        
        if mode2 == POSITIION_MODE:
            b = self.memory[b]
        elif mode2 == RELATIVE_MODE:
            b = self.memory[b + self.rbase]

        if mode3 == RELATIVE_MODE:
            c += self.rbase
        return (a,b,c)
        
    
    def run(self):
        while self.running:
            opcode, mode1, mode2, mode3 = decode(self.memory[self.pc])
            a,b,c = self.getParams()
            if opcode == 99:
                self.running = False
            elif opcode == 1:
                # add
                self.memory[c] = a + b
                self.pc += 4
            elif opcode == 2:
                # multiply
                self.memory[c] = a * b
                self.pc += 4
            elif opcode == 3:
                # input
                a = self.memory[self.pc+1]
                if (self.memory[self.pc] // 100) % 10 == 2:
                    a += self.rbase
                self.memory[a] = self.input
                self.pc += 2
            elif opcode == 4:
                # output
                self.pc += 2
                return a
            elif opcode == 5:
                # jump-if-true
                if a != 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 6:
                # jump-if-false
                if a == 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 7:
                # less than
                if a < b:
                    self.memory[c] = 1
                else:
                    self.memory[c] = 0
                self.pc += 4
            elif opcode == 8:
                # equals
                if a == b:
                    self.memory[c] = 1
                else:
                    self.memory[c] = 0
                self.pc += 4
            elif opcode == 9:
                # adjust relative base
                self.rbase += a
                self.pc += 2
        
        return 0

m = Machine(code)
grid = defaultdict(int)
grid[(0,0)] = 1
x, y = 0, 0
maxx = 0
maxy = 0
heading = 0
while m.running:
    m.input = grid[(x,y)]
    color = m.run()
    turn = m.run()
    if turn == 0:
        heading = (heading - 1) % 4
    else:
        heading = (heading + 1) % 4
    grid[(x,y)] = color
    if heading == 0:
        # North
        y -= 1
    elif heading == 1:
        # East
        x += 1
    elif heading == 2:
        # South
        y += 1
    elif heading == 3:
        # West
        x -= 1
    maxx = max(maxx, x)
    maxy = max(maxy, y)

answer = [[grid[(x,y)] for x in range(maxx+1)] for y in range(maxy+1)]
for line in answer:
    print(''.join('.#'[v] for v in line))