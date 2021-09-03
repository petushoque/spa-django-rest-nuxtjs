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

# удалить из исходного списка самый короткий элемент, чтобы дальше сравнивать его с остальным списком
s.remove(min_elem)

res = ''
for i in range(min_len):
    counter = 0
    for j in range(len(s)):        
        #print(min_elem[i], s[j][i])
        if min_elem[i] == s[j][i]:
            counter += 1
        if counter == len(s):
            res += min_elem[i]
            counter = 0   
if res != 0:
    print(res)