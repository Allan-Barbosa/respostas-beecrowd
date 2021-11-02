c, q = input().split(" ")
c = int(c)
q = int(q)
v = 0
if(c == 1):
    v = q*4.00
if(c == 2):
    v = q*4.50
if(c == 3):
    v = q*5.00
if(c == 4):
    v = q*2.00
if(c == 5):
    v = q*1.50
print("Total: R$ %.2f" % v)
