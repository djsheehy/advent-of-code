import re
from collections import Counter
pattern = re.compile(r"([a-z]+(?:-[a-z]+)*)-(\d+)\[([a-z]+)\]")

def real(txt):
    m = pattern.match(txt)
    name = ''.join(filter(str.isalpha, m.group(1)))
    sector = int(m.group(2))
    checksum = m.group(3)
    sortedPairs = sorted(Counter(name).items(), key=lambda x: (-x[1], x[0]))
    check = (''.join(p[0] for p in sortedPairs))[:5]
    if check == checksum:
        return (name, sector)
    else:
        return None

def decrypt(name, rotate):
    return ''.join(chr((ord(c)-97+rotate)%26+97) for c in name)

with open("input04.txt") as f:
    lines = map(str.strip, f)
    realRooms = list(filter(lambda x: x, map(real, lines)))
    print("part 1:", sum(room[1] for room in realRooms))
    for room in realRooms:
        if 'northpole' in decrypt(*room):
            print('part 2:',room[1])
            break
        
