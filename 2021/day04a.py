class Bingo:
    def __init__(self, board):
        self.board = [[int(n) for n in row.split()] for row in board.split("\n")]
        self.skip = False
    
    def winner(self):
        for row in self.board:
            if all(n == -1 for n in row):
                self.skip = True
                return True
        for i in range(5):
            column = [self.board[j][i] for j in range(5)]
            if all(n == -1 for n in column):
                self.skip = True
                return True
        return False
    
    def draw(self, n):
        for r, row in enumerate(self.board):
            for c, num in enumerate(row):
                if num == n:
                    self.board[r][c] = -1
    
    def unmarked_sum(self):
        ans = 0
        for row in self.board:
            ans += sum(x for x in row if x != -1)
        return ans


f = open('input04.txt')
numbers = map(int, next(f).strip().split(','))
next(f)
boards = [Bingo(b) for b in f.read().strip().split("\n\n")]

def main():
    for n in numbers:
        for b in boards:
            b.draw(n)
            if b.winner():
                return b.unmarked_sum() * n

if __name__ == '__main__':
    print(main())