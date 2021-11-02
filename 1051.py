s = float(input())
s = round(s, 2)
i = 0
x = 0
y = 0
z = 0
if(s <= 2000):
    print("Isento")
if(s > 2000 and s <= 3000):
    i = ((s-2000)*0.08)
    print("R$ %.2f" % i)
if(s > 3000 and s <= 4500):
    x = (s-3000)*0.18
    y = 1000*0.08
    i = x+y
    print("R$ %.2f" % i)
if(s > 4500):
    x = 1000*0.08
    y = 1500*0.18
    z = (s-4500)*0.28
    i = x+y+z
    print("R$ %.2f" % i)
