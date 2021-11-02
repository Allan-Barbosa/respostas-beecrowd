n = int(input())
x = 0
for i in range(1, n+1):
    z = 0
    x = i
    aux = x
    while True:
        z += 1
        if z == 3:
            print(x)
            break
        print('{} '.format(x), end='')
        x = x*aux
