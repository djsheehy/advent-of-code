f = open('input04.txt')
passports = f.read().strip().split('\n\n')
f.close()
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
answer = 0
for pp in passports:
    myfields = set()
    for line in pp.splitlines():
        for field in line.split(' '):
            key = field.split(':')[0]
            myfields.add(key)
    myfields.add('cid')
    if myfields == fields:
        answer += 1
print(answer)