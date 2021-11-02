a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)
x = 0
y = 0
if(b > a and b > c):
    x = a
    a = b
    b = x
if(c > a and c > b):
    x = a
    a = c
    c = x
if(b < c):
    y = b
    b = c
    c = y
if(a >= b+c):
    print("NAO FORMA TRIANGULO")
if((a**2) == (b**2+c**2)):
    print("TRIANGULO RETANGULO")
if((a*a) > (b*b+c*c) and a < (b+c)):
    print("TRIANGULO OBTUSANGULO")
if((a**2) < ((b**2)+(c**2))):
    print("TRIANGULO ACUTANGULO")
if(a == b and a == c):
    print("TRIANGULO EQUILATERO")
if(a == b and b != c or b == c and c != a or a == c and c != b):
    print("TRIANGULO ISOSCELES")
