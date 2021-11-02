while True:
    try:
        n = int(input())
        l = input().split(' ')
        for k in range(n):
            l[k] = int(l[k])
        lm = 0
        for i in range(n):
            if l[i] > lm:
                lm = l[i]
        if lm < 10:
            print('1')
        elif lm > 10 and lm < 20:
            print('2')
        elif lm >= 20:
            print('3')
    except EOFError:
        break
