a = int(input())
b = int(input())
tmp = str(a + b)
print(tmp)

for i in range(len(tmp) - 1, -1, -1):
    print(tmp[i])
