n = int(input())
c = 10000
x = 0
while(c >= 1):
    c -= 1
    x += 1
    if(x % n == 2):
        print(x)
