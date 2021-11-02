entrada = input()
valores = entrada.split(" ")
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
A = a
B = b
C = c
if a > b:
    x = a
    a = b
    b = x
if a > c:
    y = a
    a = c
    c = y
if b > c:
    z = b
    b = c
    c = z
print("""{a}
{b}
{c}

{A}
{B}
{C}""".format(a=a, b=b, c=c, A=A, B=B, C=C))
