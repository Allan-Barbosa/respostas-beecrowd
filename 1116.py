n = int(input())
for z in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if(y != 0):
        r = x/y
        print('{:.1f}'.format(r))
    else:
        print('divisao impossivel')
