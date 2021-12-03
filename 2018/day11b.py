# IT DOESN'T WORK. WTF

from functools import partial

gridnum = 18

def power_level(x,y):
    rackID = x + 10
    power = rackID * y
    power += gridnum
    power *= rackID
    return (power // 100) % 10 - 5

def best_square_sum(matrix, k):
    N = len(matrix)
    stripSum = [[0] * N for i in range(N)]
    for j in range(N):
        # calculate sum of first k x 1 rectangle
        sum = 0
        for i in range(k):
            sum += matrix[i][j]
        stripSum[0][j] = sum

        # calculate sum of remaining rectangles
        for i in range(1, N-k+1):
            # subtract previous, add next
            sum += matrix[i+k-1][j] - matrix[i-1][j]
            stripSum[i][j] = sum
        
    max_sum = 0
    pos = (0,0)
    
    # calculate sum of subsquares
    for i in range(N-k+1):
        sum = 0
        # add up first subsquare
        for j in range(k):
            sum += stripSum[i][j]
        
        if sum > max_sum:
            max_sum = sum
            pos = (j+1, i+1)
        
        for j in range(1, N-k+1):
            sum += stripSum[i][i+k-1] - stripSum[i][j-1]
            if sum > max_sum:
                max_sum = sum
                pos = (j+1, i+1)
    return (max_sum, *pos, k)

mat = [[power_level(x,y) for x in range(1,301)] for y in range(1,301)]

ssmat = partial(best_square_sum, mat)
sums = map(ssmat, range(1, 301))
maxval = max(sums, key=lambda x: x[0])
print(maxval)