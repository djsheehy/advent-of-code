from sys import exit

f = open("input01.txt")
nums = [int(x) for x in f]
for i, x in enumerate(nums):
    for j, y in enumerate(nums):
        if i != j and x + y == 2020:
            print(x*y)
            exit()