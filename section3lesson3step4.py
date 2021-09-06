nums = input().split(',')
res = [int(nums[0])]
for i in range(1, len(nums)):
    if int(nums[i]) != int(nums[i - 1]):
        res.append(int(num[i]))
print(nums)