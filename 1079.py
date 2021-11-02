c = int(input())
n = []
n1 = "c"
n2 = "n"
n3 = "a"
while(c >= 1):
    n = input().split(" ")
    n1, n2, n3 = round(float(n[0]), 2), round(
        float(n[1]), 2), round(float(n[2]), 2)
    m = ((n1*2)+(n2*3)+(n3*5))/(2+3+5)
    print("%.1f" % m)
    c -= 1
