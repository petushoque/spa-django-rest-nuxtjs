#Напишите программу, которая находит самый длинный общий префикс для строк находящихся в списке строк
#flower,flow,flight
s = input().split(',')

# найти самый короткий элемент
min_elem = s[0]
min_len = 100
for i in range(len(s)):
    if len(s[i]) < min_len:
        min_len = len(s[i])
        min_elem = s[i]

print(min_elem, min_len)

# удалить из исходного списка самый короткий элемент, чтобы дальше сравнивать его с остальным списком
s.remove(min_elem)

print(s)

res = ''
for i in range(len(s)):
    counter = 0
    for j in range(min_len):        
        print(s[0][i], s[j][i])
        
        if s[0][i] == s[j][i]:
            counter += 1
            print('yes')
        if counter == len(s):
            res += s[0][i]
            counter = 0
        print(counter)
        print(res)
        
print(res)