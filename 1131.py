g = 0
vi = 0
vg = 0
e = 0
v = 0
x = 1
while(x == 1):
    gi, gg = input().split(' ')
    gi = int(gi)
    gg = int(gg)
    if(gi > gg):
        vi += 1
    if(gg > gi):
        vg += 1
    if(gg == gi):
        e += 1
    g += 1
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
print('''{g} grenais
Inter:{vi}
Gremio:{vg}
Empates:{e}'''.format(g=g, vi=vi, vg=vg, e=e))
if(vi == vg):
    print('Nao houve vencedor')
if(vi > vg):
    print('Inter venceu mais')
if(vg > vi):
    print('Gremio venceu mais')
