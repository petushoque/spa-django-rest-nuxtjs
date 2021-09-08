#Дан массив чисел nums и число k. Определите есть ли в массиве такие числа дубликаты, чтобы между ними было расстояние k.
nums = [int(i) for i in  input().split(',')]
print(nums)
k = int(input())
print(k)

has_double = False

for i in range(k, len(nums)):
    print(nums[i], nums[i - (k + 1)])
    if nums[i] == nums[i - k]:
        print('yes')