c = 100
x = 0
c2 = 0
while(c >= 1):
    n = int(input())
    c2 += 1
    if(n > x):
        c3 = c2
    if(n > x):
        x = n
    else:
        n = x
    c -= 1
if(x > n):
    print(x)
    print(c3)
else:
    print(n)
    print(c3)
