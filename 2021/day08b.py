f = open('input08.txt')
pairs = [line.strip().split(' | ') for line in f]
f.close()

#  000
# 1   2
# 1   2
#  333
# 4   5
# 4   5
#  666

def decode(input, output):
    input = [set(d) for d in input.split()]
    output = [set(d) for d in output.split()]
    digits = [0] * 10
    # Get digits 1, 4, 7, 8 based on number of segments
    for d in input:
        ld = len(d)
        if ld == 2:
            digits[1] = d
        elif ld == 3:
            digits[7] = d
        elif ld == 4:
            digits[4] = d
        elif ld == 7:
            digits[8] = d
    segments = [0] * 7
    # 2, 3, and 5 have 5 segments
    fiveseg = [d for d in input if len(d) == 5]
    # if the digit contains both segments from digit 1, it's 3
    for d in fiveseg:
        if digits[1].issubset(d):
            digits[3] = d
            break
    
    # the segment in d4 not in d3 is s1
    segments[1] = (digits[4]-digits[3]).pop()
    fiveseg.remove(digits[3])
    # identify d2 and d5
    for d in fiveseg:
        if segments[1] in d:
            digits[5] = d
        else:
            digits[2] = d
    
    # identify s2 and s5
    for seg in digits[1]:
        if seg in digits[2]:
            segments[2] = seg
        else:
            segments[5] = seg
    
    # remove s2 and s5 from d7 and you get s0
    segments[0] = (digits[7] - set([segments[2], segments[5]])).pop()
    # The 6 segment digits are 0, 6, and 9
    sixseg = [d for d in input if len(d) == 6]
    nine = set(digits[5])
    nine.add(segments[2])
    digits[9] = nine
    for d in sixseg:
        if segments[2] not in d:
            digits[6] = d
    sixseg.remove(digits[6])
    sixseg.remove(digits[9])
    digits[0] = sixseg.pop()
    
    lookup = dict((frozenset(d), i) for i, d in enumerate(digits))
    ans = 0
    for d in output:
        ans = ans * 10 + lookup[frozenset(d)]
    return ans

ans = 0
for input, output in pairs:
    ans += decode(input, output)

print(ans)