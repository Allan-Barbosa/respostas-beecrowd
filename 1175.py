x = []
for i in range(20):
    a = int(input())
    x.append(a)
x.reverse()
for i in range(20):
    print('N[{i}] = {x}'.format(i=i, x=x[i]))
