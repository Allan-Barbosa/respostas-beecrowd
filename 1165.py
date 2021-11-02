t = 0
n = int(input())
for i in range(n):
    x = int(input())
    for z in range(2, x):
        if x % z == 0:
            t += 1
    if t == 0:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
    t = 0
