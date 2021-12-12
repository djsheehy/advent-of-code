data = [[int(n) for n in row.strip()] for row in open('input09.txt')]
width = len(data[0])
height = len(data)

def riskLevel(row, col):
    n = data[row][col]
    if row > 0 and n >= data[row-1][col]:
        return 0
    if row < (height - 1) and n >= data[row+1][col]:
        return 0
    if col > 0 and n >= data[row][col-1]:
        return 0
    if col < (width - 1) and n >= data[row][col+1]:
        return 0
    return n + 1

answer = 0
for r in range(height):
    for c in range(width):
        answer += riskLevel(r, c)

print(answer)