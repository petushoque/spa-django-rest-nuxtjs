nums = [int(i) for i in input().split(',')]
x = int(input())

is_in_list = False

tmp = nums[0]
tmp_ind = 0
for i in range(len(nums)):
    if x == nums[i]:
        print(i)
        is_in_list = True
        break
    elif nums[i] < x:
        tmp = nums[i]
        tmp_ind = i

if not is_in_list:
    #вывести индекс + 1        
    print(tmp, tmp_ind)