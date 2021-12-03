f = open('input01.txt')
counts = set()
n = 0
nums = [int(x) for x in f]

while True:
    for i in nums:
        n += i
        if n in counts:
            print(n)
            quit()
        counts.add(n)