n = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
v = n % 2
v2 = n2 % 2
v3 = n3 % 2
v4 = n4 % 2
v5 = n5 % 2
c = 0
if(v == 0):
    c = c+1
if(v2 == 0):
    c = c+1
if(v3 == 0):
    c = c+1
if(v4 == 0):
    c = c+1
if(v5 == 0):
    c = c+1
print("%d valores pares" % c)
