nums = [int(i) for i in input().split(',')]
x = int(input())
print(nums, x)

tmp = nums[0]
tmp_ind = 0
for i in range(len(nums)):
    if x == nums[i]:
        print(i)
        break
    elif nums[i] < x:
        tmp = nums[i]
        tmp_ind = i
        
print(tmp, tmp_ind)