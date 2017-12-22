from collections import deque

def ones(n):
    ans = 0
    while n > 0:
        ans += n & 1
        n >>= 1
    return ans

def isopen(x, y):
    n = ones(x*x + 3*x + 2*x*y + y + y*y + 1358)
    return not (n&1)

def bfs(start):
    Q = deque([start])
    steps = {start: 0}
    def visit(x,y,n):
        if isopen(x,y) and (x,y) not in steps:
            steps[(x,y)] = n
            Q.appendleft((x,y))
            
    while Q:
        x,y = Q.pop()
        n = steps[(x,y)]+1
        if x > 0:
            visit(x-1,y,n)
        if y > 0:
            visit(x,y-1,n)
        visit(x+1,y,n)
        visit(x,y+1,n)
    return steps

steps = bfs((1,1))
print(len([x for x in steps.items() if x[1] <= 50]))
