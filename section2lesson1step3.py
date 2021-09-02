#Напишите программу, которая находит самый длинный общий префикс для строк находящихся в списке строк
#flower,flow,flight
s = input().split(',')
print(s)

# найти самый короткий элемент
min_elem = s[0]
min_len = 100
for i in range(len(s)):
    if len(s[i]) < min_len:
        min_len = len(s[i])
        min_elem = s[i]

print(min_elem, min_len)
res = ''
#for i in range(len(s[0])):
#    for j in range(len(s[0])):
#        counter = 0
#        if s[0][i] == s[j][i]:
#            counter += 1
#        if counter == len(s):
#            res += s[0][i]

print(s)