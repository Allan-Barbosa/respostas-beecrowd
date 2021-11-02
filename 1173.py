a = int(input())
x = [a]
anterior = a
for i in range(9):
    novo = anterior*2
    x.append(novo)
    anterior = novo
for i in range(10):
    print('N[{i}] = {K}'.format(i=i, K=x[i]))
