n = int(input())
z = 0
while(n >= 1):
    z = 0
    n -= 1
    x, y = input().split(" ")
    x, y = int(x), int(y)
    if(x < y):
        if(x % 2 == 0):
            x += 1
            while(x < y):
                z += x
                x += 2
        else:
            x += 2
            while(x < y):
                z += x
                x += 2
    else:
        if(y % 2 == 0):
            y += 1
            while(y < x):
                z += y
                y += 2
        else:
            y += 2
            while(y < x):
                z += y
                y += 2
    print(z)
