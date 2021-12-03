data = [l.strip().split(" contain ") for l in open("input07.txt")]
bags = {}
for outer, inner in data:
    outer = ' '.join(outer.split()[:2])
    items = inner.split(', ')
    words = [b.split() for b in items]
    items = [w[1] + ' ' + w[2] for w in words]
    items = [b for b in items if b != 'other bags.']
    bags[outer] = items

parents = {}
for key in bags.keys():
    parents[key] = set()
for key, val in bags.items():
    for b in val:
        parents[b].add(key)

visited = set()
q = ['shiny gold']
while q:
    node = q.pop()
    for n in parents[node]:
        if n not in visited:
            visited.add(n)
            q.append(n)
print(len(visited))