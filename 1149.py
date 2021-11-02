r = 0
l = input()
l = l.split(' ')
a = int(l[0])
n = int(l[-1])
for i in range(0, n):
    r += a+i
print(r)
