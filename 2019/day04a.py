puzzle = [137683, 596253]

def test(n):
    s = str(n)
    pair = False
    for i in range(1, 6):
        if ord(s[i]) < ord(s[i-1]):
            return False
        if s[i] == s[i-1]:
            pair = True
    return pair

answer = 0
for n in range(*puzzle):
    if test(n):
        answer+= 1
print(answer)