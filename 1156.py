s = 0
x = 1
for i in range(1, 39+1, 2):
    s += i/x
    x = x*2
print('{:.2f}'.format(s))
