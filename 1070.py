x = int(input())
c = 0
if(x % 2) != 0:
    while(c < 6):
        print(x)
        x += 2
        c += 1
else:
    x += 1
    while(c < 6):
        print(x)
        x += 2
        c += 1
