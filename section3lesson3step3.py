x = input().split(',')
y = input().split(',')
print(list(x))
print(list(y))

res = []

while len(x) or len(y) > 0:
    if len(x) == 0:
        print('yes')
        res.append(y)
        break
    if len(y) == 0:
        res.append(x)
        break
    if x[0] <= y[0]:
        res.append(x[0])
        x.remove(x[0])
    if y[0] > x[0]:
        res.append(y[0])
        y.remove(y[0])
print(res)