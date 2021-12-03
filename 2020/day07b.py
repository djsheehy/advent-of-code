data = [l.strip().split(" contain ") for l in open("input07.txt")]
bags = {}
for outer, inner in data:
    outer = ' '.join(outer.split()[:2])
    items = inner.split(', ')
    if 'no other bags.' in items:
        items.remove('no other bags.')
    words = [b.split() for b in items]
    items = [[int(w[0]), w[1] + ' ' + w[2]] for w in words]
    bags[outer] = items

def countbags(color):
    return 1 + sum(n * countbags(b) for n, b in bags[color])

answer = countbags('shiny gold')
print(answer-1)