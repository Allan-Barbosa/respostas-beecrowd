n1 = int(input())
n2 = int(input())
x = 0
s = 0
if n1 > n2:
    x = n1
    n1 = n2
    n2 = x
for y in range(n1, n2+1):
    if y % 13 != 0:
        s += y
print(s)
