s = 0
n = int(input())
for i in range(n):
    x = int(input())
    for z in range(1, x):
        if x % z == 0:
            s += z
    if s == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
    s = 0
