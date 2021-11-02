nc = int(input())
c = input().split(' ')
for i in range(nc):
    c[i] = int(c[i])
nf = c.count(0)
r = nc-nf
print(r)
