s = round(float(input()), 2)
x = 0
y = 0
if(s >= 0 and s <= 400):
    x = s*0.15
    y += s+s*0.15
    print("Novo salario: %.2f" % y)
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 15 %")
if(s > 400 and s <= 800):
    x = s*0.12
    y += s+s*0.12
    print("Novo salario: %.2f" % y)
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 12 %")
if(s > 800 and s <= 1200):
    x = s*0.1
    y += s+s*0.1
    print("Novo salario: %.2f" % y)
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 10 %")
if(s > 1200 and s <= 2000):
    x = s*0.07
    y += s+s*0.07
    print("Novo salario: %.2f" % y)
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 7 %")
if(s > 2000):
    x = s*0.04
    y += s+s*0.04
    print("Novo salario: %.2f" % y)
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 4 %")
