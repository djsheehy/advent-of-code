keypad = """..1..
.234.
56789
.ABC.
..D..""".split('\n')
with open("input02.txt") as f:
    row, col = 2, 0
    moves = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
    code = []
    for line in map(str.strip, f):
        for cmd in line:
            move = moves[cmd]
            r = row + move[0]
            c = col + move[1]
            if r not in range(5) or c not in range(5):
                continue
            if keypad[r][c] != '.':
                row, col = r, c
        code.append(keypad[row][col])
    print(''.join(code))
