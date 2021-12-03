def path(parent, start):
    p = []
    node = start
    while node in parent:
        node = parent[node]
        p.append(node)
    return p

def get_answer(path1, path2):
    for i, node in enumerate(path1):
        try:
            return i + path2.index(node) + 2
        except:
            continue

f = open('input06.txt')
parent = {}
for line in f:
    a, b = line.strip().split(')')
    parent[b] = a
f.close()
start = parent['YOU']
goal = parent['SAN']
start_path = path(parent, start)
goal_path = path(parent, goal)
print(get_answer(start_path, goal_path))