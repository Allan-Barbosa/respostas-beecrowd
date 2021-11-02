s = 0
n = int(input())
for i in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if x % 2 != 0:
        for i in range(y):
            s += x
            x += 2
    else:
        x += 1
        for i in range(y):
            s += x
            x += 2
    print(s)
    s = 0
