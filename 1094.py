n = int(input())
t = 0
qc = 0
qr = 0
qs = 0
while(n >= 1):
    n -= 1
    q, to = input().split(" ")
    q = int(q)
    t += q
    if(to == "C"):
        qc += q
    if(to == "R"):
        qr += q
    if(to == "S"):
        qs += q
pc = (100*qc)/t
pr = (100*qr)/t
ps = (100*qs)/t
print("Total: %d cobaias" % t)
print("Total de coelhos: %d" % qc)
print("Total de ratos: %d" % qr)
print("Total de sapos: %d" % qs)
print("Percentual de coelhos: %.2f %%" % pc)
print("Percentual de ratos: %.2f %%" % pr)
print("Percentual de sapos: %.2f %%" % ps)
