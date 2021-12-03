f = open("input02.txt")
lines = [s.split() for s in f]
answer = 0
for line in lines:
    lower, upper = [int(x) for x in line[0].split('-')]
    target = line[1][0]
    password = line[2]
    count = password.count(target)
    if count >= lower and count <= upper:
        answer += 1
print(answer)