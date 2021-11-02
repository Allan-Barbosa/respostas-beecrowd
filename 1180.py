c = int(input())
x = input().split(' ')
x[0] = int(x[0])
menor = x[0]
for i in range(c):
    x[i] = int(x[i])
    if x[i] < menor:
        menor = x[i]
posicao = x.index(menor)
print('''Menor valor: {menor}
Posicao: {posicao}'''.format(menor=menor, posicao=posicao))
