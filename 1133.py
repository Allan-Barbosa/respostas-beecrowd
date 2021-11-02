n1 = int(input())
n2 = int(input())
if(n1 > n2):
    x = n1
    n1 = n2
    n2 = x
for z in range(n1+1, n2):
    if z % 5 == 2 or z % 5 == 3:
        print(z)
