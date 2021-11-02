l1, l2, l3 = input().split(" ")
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)
p = 0
a = 0
if(l1 > abs(l2-l3) and l1 < (l2+l3) or l2 > abs(l1-l3) and l2 < (l1+l3) or l3 > abs(l2-l1) and l3 < (l2+l1)):
    p = l1+l2+l3
    print("Perimetro = %.1f" % p)
else:
    a = ((l1+l2)*l3)/2
    print("Area = %.1f" % a)
