par = []
impar = []
for i in range(15):
    elemento = int(input())
    if elemento % 2 == 0:
        par.append(elemento)
    else:
        impar.append(elemento)
    if len(par) == 5:
        for p in range(5):
            print('par[{i}] = {x}'.format(i=p, x=par[p]))
        par.clear()
    if len(impar) == 5:
        for p in range(5):
            print('impar[{i}] = {x}'.format(i=p, x=impar[p]))
        impar.clear()
for i in range(len(impar)):
    print('impar[{i}] = {x}'.format(i=i, x=impar[i]))
for i in range(len(par)):
    print('par[{i}] = {x}'.format(i=i, x=par[i]))
