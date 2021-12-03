INPUT = 1

def decode(n):
    "Decode an opcode"
    opcode = n % 100
    mode1 = (n // 100) % 10
    mode2 = (n // 1000) % 10
    return (opcode, mode1, mode2)

f = open('input05.txt')
program = f.readline().strip().split(',')
f.close()
program = [int(code) for code in program]

pc = 0 # program counter
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
        program[program[pc + 1]] = INPUT
        pc += 2
    elif opcode == 4:
        print(program[program[pc + 1]])
        pc += 2