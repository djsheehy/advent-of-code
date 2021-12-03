from itertools import permutations

f = open('input07.txt')
program = f.readline().strip().split(',')
program = [int(n) for n in program]
f.close()

test1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
test2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
def decode(n):
    "Decode an opcode"
    opcode = n % 100
    mode1 = (n // 100) % 10
    mode2 = (n // 1000) % 10
    return (opcode, mode1, mode2)

def run(code, settings):
    pc = 0 # program counter
    it = iter(settings)
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
            try:
                program[program[pc + 1]] = next(it)
            except:
                program[program[pc + 1]] = output
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

answer = 0
for p in permutations([5,6,7,8,9]):
    x = run(test1, p)
    answer = max(x, answer)

print(answer)