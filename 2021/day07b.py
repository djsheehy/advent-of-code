data = [int(x) for x in open('input07.txt').read().strip().split(',')]

def triangle(n):
    return (n * (n + 1)) // 2

def fuel(a, b):
    return triangle(abs(a-b))

def fuelSum(pos):
    return sum(fuel(pos, n) for n in data)

print(min(fuelSum(pos) for pos in range(min(data), max(data))))
