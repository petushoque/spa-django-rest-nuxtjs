x = input().split(',')
y = input().split(',')
print(list(x))
print(list(y))

res = []

while len(x) or len(y) > 0:
    print('before ', x, y)
    if len(x) == 0:
        print('yes')
        res.append(y)
        break
    if len(y) == 0:
        res += x
        break
    if int(x[0]) <= int(y[0]):
        res.append(x[0])
        x = x[1:]
    elif int(y[0]) < int(x[0]):
        res.append(y[0])
        y  = y[1:]
    print('after ', x, y)
    print('result on this iteration', res)
print(res)