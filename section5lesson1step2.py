# Дана строка. Найдите первый неповторяющийся символ в этой строке и верните его индекс. Если такого элемента нет, то верните -1 (минус один).
s = input()

res = ''

for c in s:
    if s.count(c) == 1:
        res = c
    if len(res) > 0:
        break

if len(res) > 0:
    print(s.find(res))
else:
    print(-1)