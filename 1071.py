x = int(input())
y = int(input())
s = 0
if(x < y):
    if(x % 2) == 0:
        x += 1
        while(x < y):
            s = s+x
            x += 2
    else:
        x += 2
        while(x < y):
            s = s+x
            x += 2
if(x > y):
    if(y % 2) == 0:
        y += 1
        while(y < x):
            s = s+y
            y += 2
    else:
        y += 2
        while(y < x):
            s = s+y
            y += 2
print(s)
