with open("input12.txt") as f:
    code = [line.split() for line in list(map(str.strip, f))]
    register = dict((c,0) for c in 'abcd')
    register['c'] = 1
    pc = 0
    while pc < len(code):
        cmd = code[pc]
        if cmd[0] == 'cpy':
            x, y = cmd[1:]
            if x in 'abcd':
                register[y] = register[x]
            else:
                register[y] = int(x)
        elif cmd[0] == 'inc':
            x = cmd[1]
            register[x] += 1
        elif cmd[0] == 'dec':
            x = cmd[1]
            register[x] -= 1
        elif cmd[0] == 'jnz':
            x, y = cmd[1:]
            if x in 'abcd':
                x = register[x]
            else:
                x = int(x)
            if x != 0:
                pc += int(y)
                continue
        pc += 1
    print(register['a'])
