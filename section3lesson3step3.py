x = input().split(',')
y = input().split(',')
print(list(x))
print(list(y))

res = []

while len(x) or len(y) > 0:
    print(x, y)
    if len(x) == 0:
        print('yes')
        res.append(y)
        break
    if len(y) == 0:
        res.append(x)
        break
    if int(x[0]) <= int(y[0]):
        res.append(x[0])
        del x[0]
    if int(y[0]) > int(x[0]):
        res.append(y[0])
        del y[0]
print(res)