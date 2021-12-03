from math import ceil

f = open('input14.txt')
data = []
for line in f:
    line = line.strip()
    left, right = line.split(' => ')
    inputs = [(int(n), chem) for n, chem in [s.split(' ') for s in left.split(', ')]]
    output = right.split(' ')
    output[0] = int(output[0])
    data.append((inputs, output))

recipes = {}
for inputs, output in data:
    recipes[output[1]] = {'inputs': inputs, 'amount': output[0]}

def multiply(inputs, n):
    return [(x*n, name) for x, name in inputs]

result = recipes['FUEL']['inputs']
