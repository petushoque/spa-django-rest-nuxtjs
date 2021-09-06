nums = [int(i) for i in input().split(',')]
x = int(input())
print(nums, x)

tmp = nums[0]
for i in range(len(nums)):
    if x == nums[i]:
        print(i)
        break