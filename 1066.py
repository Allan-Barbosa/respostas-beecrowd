par = 0
impar = 0
positivo = 0
negativo = 0
contador = 0
while(contador < 5):
    n = int(input())
    r = n % 2
    if(r == 0):
        par = par+1
    else:
        impar = impar+1
    if(n > 0):
        positivo = positivo+1
    if(n < 0):
        negativo = negativo+1
    contador = contador+1
print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % positivo)
print("%d valor(es) negativo(s)" % negativo)
