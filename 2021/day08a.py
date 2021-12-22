f = open('input08.txt')
answer = 0
for line in f:
    left, right = line.strip().split(' | ')
    digits = right.split()
    for d in digits:
        if len(d) in [2, 3, 4, 7]:
            answer += 1
print(answer)