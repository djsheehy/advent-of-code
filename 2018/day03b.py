import re

data = open('input03.txt').readlines()

class Fabric:
    def __init__(self):
        self.grid = []
        for i in range(1000):
            self.grid.append([0]*1000)
    
    def mark(self, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                self.grid[i][j] += 1
    
    def check(self, x, y, width, height):
        for i in range(y, y+height):
            for j in range(x, x+width):
                if self.grid[i][j] > 1:
                    return False
        return True

fab = Fabric()
claims = []
for line in data:
    nums = re.findall(r'\d+', line)
    nums = [int(x) for x in nums]
    claims.append(nums)
    fab.mark(*(nums[1:]))

for c in claims:
    if fab.check(*c[1:]):
        print(c[0])
        break