m = 0
c = 0
while True:
    x = int(input())
    if x < 0:
        break
    m += x
    c += 1
m = m/c
print('{:.2f}'.format(m))
