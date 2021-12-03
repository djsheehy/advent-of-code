from vm import Machine

f = open('input13.txt')
code = [int(c) for c in f.read().strip().split(',')]
f.close()

m = Machine(code)
answer = 0
while m.running:
    x = m.run()
    y = m.run()
    tile = m.run()
    print(f"{(x,y)} = {tile}")
    if tile == 2:
        answer += 1

print(answer)