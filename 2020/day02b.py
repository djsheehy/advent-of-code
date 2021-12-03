lines = [x.split() for x in open('input02.txt')]

answer = 0
for line in lines:
    pos1, pos2 = [int(x) for x in line[0].split('-')]
    pos1 -= 1
    pos2 -= 1
    target = line[1][0]
    password = line[2]
    answer += (password[pos1] == target) ^ (password[pos2] == target)
print(answer)
