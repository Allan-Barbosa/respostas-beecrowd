A = []
for i in range(100):
    b = float(input())
    A.append(b)
c = 0
for j in A:
    if j <= 10:
        print('A[{c}] = {j:.1f}'.format(c=c, j=j))
    c += 1
