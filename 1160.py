t = int(input())
te = 0
for z in range(t):
    pa, pb, g1, g2 = input().split(' ')
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1), float(g2)
    while(pa <= pb):
        pa = pa+((pa*g1)/100)
        pa = int(pa)
        pb = pb+((pb*g2)/100)
        pb = int(pb)
        te += 1
        if(te > 100):
            print('Mais de 1 seculo.')
            break
    if(te <= 100):
        print('{} anos.'.format(te))
    te = 0
