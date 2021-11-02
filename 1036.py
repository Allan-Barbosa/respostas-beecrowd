a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
d = (b**2)-4*a*c
if(a == 0 or b == 0 or c == 0):
    print("Impossivel calcular")
else:
    if(d < 0):
        print("Impossivel calcular")
    else:
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d**0.5)/(2*a)
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
