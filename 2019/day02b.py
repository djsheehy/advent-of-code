f = open('input02.txt')
code = f.readline().strip()
f.close()
code = list(map(int, code.split(',')))

def run(noun, verb):
    program = list(code)
    program[1] = noun
    program[2] = verb
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
    return program[0]

running = True
for noun in range(100):
    if not running:
        break
    for verb in range(100):
        if not running:
            break
        #print(f'Trying {noun},{verb}')
        output = run(noun, verb)
        if output == 19690720:
            running = False
            print(100 * noun + verb)
            break
