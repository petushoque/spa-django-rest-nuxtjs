x = input().split(',')
y = input().split(',')
print(list(x))
print(list(y))

res = []

while len(x) or len(y) > 0:
    if len(x) == 0:
        res += y
    if len(y) == 0:
        res += x
    