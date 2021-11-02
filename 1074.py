c = int(input())
x = "a"
y = "b"
while(c >= 1):
    c -= 1
    n = int(input())
    if(n % 2 == 0):
        x = "EVEN"
    else:
        x = "ODD"
    if(n > 0):
        y = "POSITIVE"
    if(n < 0):
        y = "NEGATIVE"
    if(n != 0):
        print(x, y)
    if(n == 0):
        print("NULL")
