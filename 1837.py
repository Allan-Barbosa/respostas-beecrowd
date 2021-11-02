a, b = input().split(' ')
a, b = int(a), int(b)
if b < 0:
    q = -(a//abs(b))
    r = a % abs(b)
else:
    q = a//b
    r = a % b
print(q, r)
