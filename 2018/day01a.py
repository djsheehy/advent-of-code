f = open('input01.txt')
answer = 0
for line in f:
    answer += int(line)
print(answer)