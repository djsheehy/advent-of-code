def part2(n):
    ans = 0
    n = n // 3 - 2
    while n >= 0:
        ans += n
        n = n // 3 - 2
    return ans

f = open('input01.txt')
answer = 0
answer2 = 0
for line in f:
    n = int(line)
    n1 = n // 3 - 2
    n2 = part2(n)
    answer += n1
    answer2 += n2
f.close()
print('Part 1:', answer)
print('Part 2:', answer2)