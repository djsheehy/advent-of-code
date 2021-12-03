f = open('input02.txt')
lines = f.readlines()

def diffchars(a, b):
    diff = 0
    pos = -1
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            pos = i
    return (diff, pos)

def get_answer():
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            word1 = lines[i]
            word2 = lines[j]
            diff, pos = diffchars(word1, word2)
            if diff == 1:
                answer = list(word1)
                del answer[pos]
                return ''.join(answer)

print(get_answer())