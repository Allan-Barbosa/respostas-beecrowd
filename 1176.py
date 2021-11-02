testes = int(input())
for i in range(testes):
    fib = []
    c = int(input())
    fib.append(0)
    fib.append(1)
    for i in range(1, c):
        o = len(fib)-1
        n = fib[o]+fib[o-1]
        fib.append(n)
    print('Fib({p}) = {l}'.format(p=c, l=fib[c]))
