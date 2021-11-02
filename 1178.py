n = float(input())
n = round(n, 4)
for i in range(100):
    print('N[{i}] = {ç:.4f}'.format(i=i, ç=n))
    n = n/2
