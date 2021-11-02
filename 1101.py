n, m = input().split(" ")
n = int(n)
m = int(m)
s = 0
x = 0
y = 0
while(m > 0 and n > 0):
    s = 0
    if(n > m):
        x = n
        n = m
        m = x
    for y in range(n, m+1):
        print("%d " % y, end="")
        s += y
        if y == m:
            print("Sum=%d" % s)
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
