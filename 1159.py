while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        y = x
        x = 0
        for i in range(5):
            x += y
            y += 2
    else:
        y = x+1
        x = 0
        for i in range(5):
            x += y
            y += 2
    print(x)
