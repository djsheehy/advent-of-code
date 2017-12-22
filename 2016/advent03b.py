def valid(a,b,c):
    return (a+b) > c and (a+c) > b and (b+c) > a

with open("input03.txt") as f:
    nums = [[int(x) for x in l.split()] for l in map(str.strip, f)]
    columns = [[nums[r][c] for r in range(len(nums))] for c in range(3)]
    nums = sum(columns, [])
    triangles = [nums[i*3:i*3+3] for i in range(len(nums)//3)]
    print(len([t for t in triangles if valid(*t)]))
