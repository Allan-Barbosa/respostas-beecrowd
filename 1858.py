x = int(input())
a = input()
a = a.split(' ')
for i in range(0, len(a)):
    a[i] = int(a[i])
p = a.index(min(a))
print(p+1)
