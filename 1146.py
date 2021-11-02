while True:
    x = int(input())
    for i in range(1, x+1):
        if i < x:
            print('{} '.format(i), end='')
        else:
            print(i)
    if x == 0:
        break
