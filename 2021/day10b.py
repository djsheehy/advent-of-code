f = open('input10.txt')

def bracketScore(line):
    score = 0
    stack = []
    pairs = {'}': '{', ']': '[', ')': '(', '>': '<'}
    scoreTable = {')': 1, ']': 2, '}': 3, '>': 4}
    trans = str.maketrans('([{<', ')]}>')
    
    for current in line:
        if current in pairs.values():
            stack.append(current)
        elif stack:
            lastBracket = stack.pop()
            if pairs[current] != lastBracket:
                # skip corrupt lines, only do incomplete lines
                return 0
    stack.reverse()
    stack = ''.join(stack).translate(trans)
    for c in stack:
        score = score * 5 + scoreTable[c]
    return score

scores = [bracketScore(line.strip()) for line in f]
scores = [x for x in scores if x > 0]
scores.sort()
print(scores[len(scores)//2])