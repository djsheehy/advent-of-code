from collections import Counter

def least_common(counter):
    return min(counter.items(), key=lambda x: x[1])[0]

with open("input06.txt") as f:
    counters = [Counter() for i in range(8)]
    for line in map(str.strip, f):
        for i,c in enumerate(line):
            counters[i][c] += 1
    print(''.join(c.most_common(1)[0][0] for c in counters))
    print(''.join(map(least_common, counters)))
