max = int(input())
controle = 0
for i in range(1000):
    if controle == max:
        controle = 0
    print('N[{i}] = {x}'.format(i=i, x=controle))
    controle += 1
