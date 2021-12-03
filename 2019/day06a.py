f = open('input06.txt')
# Reverse tree. orbits[a] is parent of a
orbits = {}
for line in f:
    a, b = line.strip().split(')')
    orbits[b] = a
f.close()

answer = 0
for k in orbits:
    n = k
    while n != 'COM':
        n = orbits[n]
        answer += 1

print(answer)