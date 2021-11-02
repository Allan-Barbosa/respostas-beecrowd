hi, mi, hf, mf = input().split(" ")
hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)
hi = hi*60
hf = hf*60
xi = hi+mi
xf = hf+mf
x = 0
h = 0
m = 0
if(xf > xi):
    x = xf-xi
    h = x/60
    m = x % 60
    h, m = int(h), int(m)
    print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
else:
    xf = xf+24*60
    x = xf-xi
    h = x/60
    m = x % 60
    h, m = int(h), int(m)
    print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
