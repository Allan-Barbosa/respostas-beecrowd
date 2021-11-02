N = int(input())
c = 0
c2 = 0
while(N >= 1):
    X = int(input())
    if(X >= 10 and X <= 20):
        c += 1
    else:
        c2 += 1
    N = N-1
print("%d in" % c)
print("%d out" % c2)
