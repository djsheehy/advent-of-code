from itertools import permutations

f = open('input07.txt')
program = f.readline().strip().split(',')
program = [int(n) for n in program]
f.close()

test1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]
test3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def decode(n):
    "Decode an opcode"
    opcode = n % 100
    mode1 = (n // 100) % 10
    mode2 = (n // 1000) % 10
    return (opcode, mode1, mode2)

def run(code, inputs):
    it = iter(inputs)
    pc = 0 # program counter
    output = 0
    program = list(code)
    while True:
        opcode, mode1, mode2 = decode(program[pc])
        if opcode == 99:
            break
        elif opcode == 1:
            a, b = 0, 0
            if mode1 == 1:
                a = program[pc + 1]
            else:
                a = program[program[pc+1]]
            if mode2 == 1:
                b = program[pc + 2]
            else:
                b = program[program[pc+2]]
            c = program[pc+3]
            program[c] = a + b
            pc += 4
        elif opcode == 2:
            a, b = 0, 0
            if mode1 == 1:
                a = program[pc + 1]
            else:
                a = program[program[pc+1]]
            if mode2 == 1:
                b = program[pc + 2]
            else:
                b = program[program[pc+2]]
            c = program[pc+3]
            program[c] = a * b
            pc += 4
        elif opcode == 3:
            program[program[pc + 1]] = next(it)
            pc += 2
        elif opcode == 4:
            output = program[program[pc + 1]]
            pc += 2
        elif opcode == 5:
            # jump-if-true
            a = program[pc+1] if mode1 else program[program[pc+1]]
            b = program[pc+2] if mode2 else program[program[pc+2]]
            if a != 0:
                pc = b
            else:
                pc += 3
        elif opcode == 6:
            # jump-if-false
            a = program[pc+1] if mode1 else program[program[pc+1]]
            b = program[pc+2] if mode2 else program[program[pc+2]]
            if a == 0:
                pc = b
            else:
                pc += 3
        elif opcode == 7:
            # less than
            a = program[pc+1] if mode1 else program[program[pc+1]]
            b = program[pc+2] if mode2 else program[program[pc+2]]
            c = program[pc+3]
            if a < b:
                program[c] = 1
            else:
                program[c] = 0
            pc += 4
        elif opcode == 8:
            # equals
            a = program[pc+1] if mode1 else program[program[pc+1]]
            b = program[pc+2] if mode2 else program[program[pc+2]]
            c = program[pc+3]
            if a == b:
                program[c] = 1
            else:
                program[c] = 0
            pc += 4
    return output

def runSequence(program, seq):
    output = 0
    for phase in seq:
        output = run(program, [phase, output])
    return output

answer = 0
perm = permutations([0,1,2,3,4])
for p in perm:
    x = runSequence(program, p)
    if x > answer:
        answer = x
print(answer)