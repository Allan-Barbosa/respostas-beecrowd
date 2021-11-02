j = int(input())
st = 0
bt = 0
at = 0
st1 = 0
sb1 = 0
sa1 = 0
for i in range(j):
    n = input()
    s, b, a = input().split(' ')
    s, b, a = int(s), int(b), int(a)
    s1, b1, a1 = input().split(' ')
    s1, b1, a1 = int(s1), int(b1), int(a1)
    st += s
    bt += b
    at += a
    st1 += s1
    sb1 += b1
    sa1 += a1
ps = st1*100/st
pa = sa1*100/at
pb = sb1*100/bt
print('''Pontos de Saque: {ps:.2f} %.
Pontos de Bloqueio: {pb:.2f} %.
Pontos de Ataque: {pa:.2f} %.'''.format(ps=ps, pb=pb, pa=pa))
