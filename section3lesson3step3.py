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
        continue
    if len(y) == 0:
        res.append(x)
        continue
    if int(x[0]) <= int(y[0]):
        res.append(x[0])
        x = x[1:]
    if int(y[0]) < int(x[0]):
        res.append(y[0])
        y  = y[1:]
print(res)