n = int(input())
x = 2
q = 0
if(5 < n < 2000):
    while(x <= n):
        q = x**2
        print("%d^2 =" % x, q)
        x += 2
