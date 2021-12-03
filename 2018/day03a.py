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
    
    def answer(self):
        ans = 0
        for row in self.grid:
            for square in row:
                if square >= 2:
                    ans += 1
        return ans

fab = Fabric()
for line in data:
    nums = re.findall(r'\d+', line)[1:]
    nums = [int(x) for x in nums]
    fab.mark(*nums)
print(fab.answer())