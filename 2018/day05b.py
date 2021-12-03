import re
from string import ascii_uppercase, ascii_lowercase

f = open('input05.txt')
polymer = f.read().strip()
f.close()

pairs = list(zip(ascii_uppercase, ascii_lowercase))
pairs.extend(zip(ascii_lowercase, ascii_uppercase))
pairs = [''.join(p) for p in pairs]
pattern = re.compile('|'.join(pairs))

def react(poly, letter):
    print(letter)
    prev = ''
    poly = re.sub(letter, '', poly, flags=re.IGNORECASE)
    while prev != poly:
        prev = poly
        poly = re.sub(pattern, '', poly)
    return len(poly)

results = [react(polymer, c) for c in ascii_uppercase]
print(min(results))