distance, depth = 0, 0
with open('input02.txt') as f:
    commands = [line.strip().split() for line in f]
    for cmd, n in commands:
        n = int(n)
        if cmd == 'forward':
            distance += n
        elif cmd == 'up':
            depth -= n
        elif cmd == 'down':
            depth += n
print(distance * depth)
