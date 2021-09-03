x = int(input())
if x < 0:
    x_rev = '-' + str(x)[:0:-1]
    print(x_rev)
if x > 0:
    x_rev = str(x)[::-1]
    if int(x_rev) < 2 ** 31:
        print(x_rev)
    else:
        print(0)