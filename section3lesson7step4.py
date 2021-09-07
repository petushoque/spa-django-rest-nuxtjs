#Дан массив целых чисел, который уже отсортирован в порядке возрастания, найдите два числа, которые складываются в целевое целевое число.
#Верните индексы двух чисел таким образом (индекс начинается не с 0 как обычно, а с 1), чтобы числа под этими индексами суммировались в целевое значение. Причем индекс 1 должен быть меньше индекса 2.
x = [int(i) for i in  input().split(',')]
target = int(input())

res = []

for i in range(len(x)):
    for j in range(i, len(x)):
        if x[i] + x[j] == target:
            res.append(i + 1)
            res.append(j + 1)
            
print(res)