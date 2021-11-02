hi, hf = input().split(" ")
hi, hf = int(hi), int(hf)
if(hi == hf):
    print("O JOGO DUROU 24 HORA(S)")
if(hi < hf):
    h = hf-hi
    print("O JOGO DUROU %d HORA(S)" % h)
else:
    if(hi != hf):
        hf += 24
        h = hf-hi
        print("O JOGO DUROU %d HORA(S)" % h)
