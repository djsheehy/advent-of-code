distance, depth, aim = 0, 0, 0
with open('input02.txt') as f:
    commands = [line.strip().split() for line in f]
    for cmd, n in commands:
        n = int(n)
        if cmd == 'down':
            aim += n
        elif cmd == 'up':
            aim -= n
        elif cmd == 'forward':
            distance += n
            depth += aim * n
print(distance * depth)