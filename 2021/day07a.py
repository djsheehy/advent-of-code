data = [int(x) for x in open('input07.txt').read().strip().split(',')]

def fuel(nums, pos):
    return sum(abs(n - pos) for n in nums)

answers = map(lambda x: fuel(data, x), range(min(data), max(data)+1))
print(min(answers))