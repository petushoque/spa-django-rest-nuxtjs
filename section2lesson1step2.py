x = input().split(',')
y = int(input())
res = []
for i in range(len(x)):
    for j in range(1, len(x)):
        if int(x[i]) == int(x[j]):
            continue
        if int(x[i]) + int(x[j]) == y:
            print('yes')
            res.append(x[i])
            res.append(x[j])
            break
print(res)