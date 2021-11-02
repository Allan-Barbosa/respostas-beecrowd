n = int(input())
c = -1
j = 0
for i in range(n):
    c += 1
    z = c+1
    aux = z
    j = 0
    while True:
        j += 1
        if j == 3:
            print(z)
            z = aux
            while True:
                j += 1
                if j == 6:
                    print(z)
                    break
                print('{} '.format(z), end='')
                if j > 4:
                    z -= 1
                z = (z*aux)+1
        if j == 6:
            break
        print('{} '.format(z), end='')
        z = z*aux
