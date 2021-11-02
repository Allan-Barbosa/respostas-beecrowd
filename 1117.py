m = 0
c = 0
while c <= 1:
    n = float(input())
    if(n >= 0 and n <= 10):
        m += n
        c += 1
        if(c == 2):
            m = m/2
            print("media = %.2f" % m)
    else:
        print("nota invalida")
