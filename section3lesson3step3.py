x = input().split(',')
y = input().split(',')
print(list(x))
print(list(y))

res = []

while len(x) or len(y) > 0:
    if len(x) == 0:
        res += y
        break
    if len(y) == 0:
        res += x
        break
    if x[0] < y[0]:
        res += x[0]
    