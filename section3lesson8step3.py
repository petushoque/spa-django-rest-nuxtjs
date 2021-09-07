#Данн список чисел nums размером n.
#Верните самый часто повторяемый элемент из списка. Часто повторяемый это элемент, который появляется больше чем [n/2]

nums = [int(i) for i in  input().split(',')]
print(nums)

pop_num = 0
pop_num_count = 0

for i in range(len(nums)):
    if nums.count(nums[i]) > pop_num_count:
        pop_num = nums[i]
        pop_num_count = nums.count(i)
print(pop_num, pop_num_count)