x = input().split(',')
y = int(input())
res = []
for i in range(len(x)):
    for j in range(1, len(x)):
        if int(x[i]) == int(x[j]):
            continue
        if int(x[i]) + int(x[j]) == y:
            if i not in res:
                res.append(i)
            if j not in res:
                res.append(j)
            break
print(res)