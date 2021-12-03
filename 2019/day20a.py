f = open('input14.txt')
maze = [line.strip('\n') for line in f]
f.close()

graph = {}
for y, line in enumerate(maze[2:-2]):
    for x, c in enumerate(line[2:-2]):
        if c == '.':
            graph[(x,y)] = []
            if maze[y][x-1] == '.':
                graph[(x,y)].append((x-1,y))
            if maze[y][x+1] == '.':
                graph[(x,y)].append((x+1,y))
            if maze[y-1][x] == '.':
                graph[(x,y)].append((x,y-1))
            if maze[y+1][x] == '.':
                graph[(x,y)].append((x,y+1))

portals = {}
# scan for labels
# top
for x, c in enumerate(maze[0][2:-2]):
    if c.isalpha():
        name = maze[0][x+2] + maze[1][x+2]
        portals[name] = [(x, 0)]

# bottom

# left

# right

# inside top

# inside bottom

# inside left

# inside right