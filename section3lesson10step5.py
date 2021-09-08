#Дан массив чисел nums. Найди в этом массиве нули и подвинь их в конец. Остальные числа должны идти в том же порядке.
nums = [int(i) for i in  input().split(',')]
print(nums)

res = []
zero_counter = 0

for i in range(len(nums)):
    if nums[i] != 0:
        res.append(nums[i])

if zero_counter > 0:
    for i in range(zero_counter):
        res.append(0)
        
print(res)