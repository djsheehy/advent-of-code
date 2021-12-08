numbers = [int(x) for x in open('input06.txt').read().strip().split(',')]
# You can't store all the numbers in a growing list. It will quickly become
# huge and slow and the memory will explode. Instead count how many fish
# have each timer value. fish[n] is how many fish have value n.

fish = [numbers.count(i) for i in range(9)]

def tick(nums):
    temp = nums[0]
    for i in range(8):
        nums[i] = nums[i+1]
    nums[8] = temp
    nums[6] += temp

for i in range(256):
    tick(fish)

print(sum(fish))