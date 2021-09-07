#Дан массив чисел. Если в нем есть дубликаты, то верните True, если нет, то False.

nums = [int(i) for i in  input().split(',')]

has_double = False

for i in range(len(nums)):
    if nums.count(nums[i]) > 1:
        has_double = True
        
if has_double:
    print('True')
else:
    print('False')