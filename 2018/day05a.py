import re
from string import ascii_uppercase, ascii_lowercase

f = open('input05.txt')
polymer = f.read().strip()
f.close()

pairs = list(zip(ascii_uppercase, ascii_lowercase))
pairs.extend(zip(ascii_lowercase, ascii_uppercase))
pairs = [''.join(p) for p in pairs]
pattern = re.compile('|'.join(pairs))

prev = polymer
polymer = pattern.sub('', polymer)
while prev != polymer:
    prev = polymer
    polymer = pattern.sub('', polymer)

print(len(polymer))