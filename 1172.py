x = []
for i in range(10):
    auxiliar = int(input())
    x.append(auxiliar)
for i in range(x.count(0)):
    auxiliar = x.index(0)
    x.remove(0)
    x.insert(auxiliar, 1)
for negativo in x:
    if negativo < 0:
        auxiliar = x.index(negativo)
        x.remove(negativo)
        x.insert(auxiliar, 1)
for i in range(10):
    print('X[{i}] = {K}'.format(i=i, K=x[i]))
