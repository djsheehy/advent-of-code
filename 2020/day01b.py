from sys import exit

f = open('input01.txt')
nums = [int(x) for x in f]
for i, x in enumerate(nums):
    for j, y in enumerate(nums):
        if i == j or x + y >= 2020:
            continue
        for k, z in enumerate(nums):
            if i != k and x + y + z == 2020:
                print(x*y*z)
                exit()