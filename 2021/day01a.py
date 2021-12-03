nums = [int(n.strip()) for n in open('input01.txt')]
ans = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        ans += 1

print(ans)