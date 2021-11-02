x = int(input())
z = int(input())
c = 1
while z <= x:
    z = int(input())
y = x
j = 1
while x <= z:
    x += y+j
    c += 1
    j += 1
print(c)
