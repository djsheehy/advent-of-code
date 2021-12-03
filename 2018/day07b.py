import re
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
for v in graph.values():
    v.sort()
for v in rev.values():
    v.sort()

# while ready:
#     n = heapq.heappop(ready)
#     order.append(n)
#     heapq.heapify(graph[n])
#     while graph[n]:
#         m = heapq.heappop(graph[n])
#         rev[m].remove(n)
#         if not rev[m]:
#             heapq.heappush(ready, m)

# def itersteps(graph, rev, ready):
#     queue = list(ready)
#     while queue:
#         n = queue.pop(0)
#         yield n
#         heapq.heapify(graph[n])
#         while graph[n]:
#             m = heapq.heappop(graph[n])
#             rev[m].remove(n)
#             if not rev[m]:
#                 queue.append(m)

class Worker:
    def __init__(self):
        self.step = None
        self.seconds = 0
    
    def assign(self, step):
        self.step = step
        self.seconds = ord(step)-4
    
    def tick(self):
        self.seconds -= 1

class WorkerManager:
    def __init__(self, graph, rev):
        self.workers = [Worker() for i in range(5)]
        self.graph = graph
        self.rev = rev
        self.seconds = 0
        ready = [c for c in ABC if not rev[c]]
        for w, s in zip(self.workers, ready):
            w.assign(s)
        self.queue = []
    
    def done(self):
        return all(w.seconds == 0 for w in self.workers)
    
    def step(self):
        self.seconds += 1
        # Each worker with an assignment works 1 second.
        for w in self.workers:
            if w.seconds:
                w.tick()
        
        # For each expired worker...
        for w in filter(lambda w: w.seconds == 0, self.workers):
            # if the worker had a step when it expired,
            # delete that step from the graph and add ready steps to the queue.
            if w.step:
                n = w.step  
                while graph[n]:
                    m = graph[n].pop(0)
                    rev[m].remove(n)
                    if not rev[m]:
                        self.queue.append(m)
            if self.queue:
                w.assign(self.queue.pop(0))

wm = WorkerManager(graph, rev)
while not wm.done():
    wm.step()
print(wm.seconds)