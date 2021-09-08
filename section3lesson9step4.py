#Дан массив чисел nums и число k. Определите есть ли в массиве такие числа дубликаты, чтобы между ними было расстояние k.
nums = [int(i) for i in  input().split(',')]
k = int(input())

has_double = False

for i in range(k + 1, len(nums)):
    if nums[i] == nums[i - k]:
        has_double = True
        
        
if has_double:
    print('True')
else:
    print('False')