f = open('input10.txt')

def bracketScore(line):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '(', '>': '<'}
    scoreTable = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for current in line:
        if current in pairs.values():
            # push open brackets onto stack
            stack.append(current)
            continue
        # closed bracket...
        elif len(stack) == 0:
            # skip incomplete lines
            continue
        else:
            lastBracket = stack.pop()
            if pairs[current] == lastBracket:
                continue
            else:
                score += scoreTable[current]
    return score

answer = 0
for line in f:
    line = line.strip()
    answer += bracketScore(line)

print(answer)