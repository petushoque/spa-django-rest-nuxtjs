x = input().split(',')
y = input().split(',')

res = []

while len(x) or len(y) > 0:
    if len(x) == 0:
        res += y
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
print(res)

res_int = [int(i) for i in res]

print(res_int)