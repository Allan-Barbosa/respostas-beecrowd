x = 1
while x == 1:
    n = float(input())
    while n > 10 or n < 0:
        print('nota invalida')
        n = float(input())
    n2 = float(input())
    while n2 > 10 or n2 < 0:
        print('nota invalida')
        n2 = float(input())
    m = (n+n2)/2
    print('media = {:.2f}'.format(m))
    print('novo calculo (1-sim 2-nao)')
    x = int(input())
    if x != 1 and x != 2:
        while (x != 1 and x != 2):
            print('novo calculo (1-sim 2-nao)')
            x = int(input())
