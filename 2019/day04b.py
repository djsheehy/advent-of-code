puzzle = [137683, 596253]

def test(n):
    s = str(n)

    group = 1
    pair = False
    for i in range(1,6):
        if ord(s[i]) < ord(s[i-1]):
            return False
        if s[i] == s[i-1]:
            group += 1
        else:
            if group == 2:
                pair = True
            group = 1
    if group == 2:
        pair = True
    return pair

answer = 0
for n in range(*puzzle):
    if test(n):
        answer += 1
print(answer)