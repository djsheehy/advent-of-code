def valid(a,b,c):
    return (a+b) > c and (a+c) > b and (b+c) > a

with open("input03.txt") as f:
    triangles = [[int(x) for x in l.split()] for l in map(str.strip, f)]
    goodTris = [tri for tri in triangles if valid(*tri)]
    print(len(goodTris))
