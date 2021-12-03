f = open('input02.txt')
program = f.readline().strip()
program = list(map(int, program.split(',')))
program[1] = 12
program[2] = 2
pos = 0
while True:
    opcode = program[pos]
    if opcode == 99:
        break
    a, b, c = program[pos+1:pos+4]
    if opcode == 1:
        program[c] = program[a] + program[b]
    elif opcode == 2:
        program[c] = program[a] * program[b]
    pos += 4
print(program[0])