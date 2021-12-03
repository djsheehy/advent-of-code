import re
import heapq
from string import ascii_uppercase as ABC

f=open('input07.txt')
lines = [l.strip() for l in f.readlines()]
f.close()

pat = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
graph = dict((c, list()) for c in ABC)
rev = dict((c, list()) for c in ABC)

for l in lines:
    m = re.match(pat, l)
    a = m.group(1)
    b = m.group(2)
    graph[a].append(b)
    rev[b].append(a)

ready = [c for c in ABC if not rev[c]]
order = []
while ready:
    n = heapq.heappop(ready)
    order.append(n)
    heapq.heapify(graph[n])
    while graph[n]:
        m = heapq.heappop(graph[n])
        rev[m].remove(n)
        if not rev[m]:
            heapq.heappush(ready, m)

print(''.join(order))