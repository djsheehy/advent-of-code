from collections import Counter
data = open('input02.txt')
twos = 0
threes = 0

for line in data:
    count = Counter(line)
    vals = count.values()
    if 2 in vals:
        twos += 1
    if 3 in vals:
        threes += 1

print(twos * threes)