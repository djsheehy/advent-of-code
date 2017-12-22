class Screen:
    def __init__(self):
        self.screen = [[0]*50 for i in range(6)]

    def rect(self, width, height):
        for row in range(height):
            for col in range(width):
                self.screen[row][col] = 1

    def rotateColumn(self, x, n):
        column = [self.screen[i][x] for i in range(6)]
        for i in range(6):
            self.screen[(i+n)%6][x] = column[i]

    def rotateRow(self, y, n):
        row = list(self.screen[y])
        for i in range(50):
            self.screen[y][(i+n)%50] = row[i]

    def count(self):
        ans = 0
        for row in self.screen:
            ans += sum(row)
        return ans

    def display(self):
        for row in self.screen:
            print(''.join('#' if x else ' ' for x in row))

with open('input08.txt') as f:
    screen = Screen()
    for line in map(str.strip, f):
        words = line.split()
        if words[0] == 'rect':
            size = map(int, words[1].split('x'))
            screen.rect(*size)
        elif words[0] == 'rotate':
            a = int(words[2][2:])
            b = int(words[4])
            if words[1] == 'column':
                screen.rotateColumn(a,b)
            else:
                screen.rotateRow(a,b)
    print(screen.count())
    screen.display()
