n = int(input())
a = 1
b = 0
x = 0
c = 0
for z in range(n-1):
    if c == 0:
        print('%d ' % b, end='')
    c += 1
    if c == n-1:
        print(a)
    else:
        print('%d ' % a, end='')
    x = a
    a = a+b
    b = x
