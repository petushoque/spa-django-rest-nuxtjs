x = input().split(',')
y = float(input())
res = []
for i in range(len(x)):
    for j in range(i, len(x)):
        if float(x[i]) + float(x[j]) == y:
            res.append(i)
            res.append(j)
        if len(res) == 2:
            break
print(res)