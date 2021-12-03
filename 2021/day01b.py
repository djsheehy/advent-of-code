nums = [int(n.strip()) for n in open('input01.txt')]
last_sum = sum(nums[0:3])
ans = 0
for i in range(1, len(nums)-2):
    cur_sum = sum(nums[i:i+3])
    if cur_sum > last_sum:
        ans += 1
    last_sum = cur_sum

print(ans)