x = int(input())
x_rev = str(x)[::-1]
if x == int(x_rev):
    print('True')
else:
    print('False')