# FIXME
import re

pat_year = r"^\d{4}$"
pat_height = r"^(\d{2,3})(in|cm)$"
pat_hcl = r"^#[0-9a-f]{6}$"
pat_ecl = r"^amb|blu|brn|gry|grn|hzl|oth$"
pat_pid = r"^\d{9}$"
passports = [p.split() for p in open('input04.txt').read().split('\n\n')]
passports = map(lambda p: dict(f.split(':') for f in p), passports)
answer = 0

def validate(pp):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in pp:
            return False
    for f in ['byr', 'iyr', 'eyr']:
        if not re.match(pat_year, pp[f]):
            return False
    ranges = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030)}
    for key, (low, high) in ranges.items():
        year = int(pp[key])
        if year < low or year > high:
            return False
    
    m = re.match(pat_height, pp['hgt'])
    if not m:
        return False
    height = int(m[1])
    units = m[2]
    if units == 'cm':
        if height < 150 or height > 193:
            return False
    else:
        if height < 59 or height > 76:
            return False
    
    if not re.match(pat_hcl, pp['hcl']):
        return False
    
    if not re.match(pat_pid, pp['pid']):
        return False
    
    return True

for pp in passports:
    if validate(pp):
        answer += 1

print(answer)