x = int(input())
if x < 0:
    x_rev = '-' + str(x)[:0:-1]
    if int(x_rev) > -(2 ** 31):
        print(int(x_rev))
    else:
        print(0)    
if x > 0:
    x_rev = str(x)[::-1]
    if int(x_rev) < 2 ** 31:
        print(int(x_rev))
    else:
        print(0)