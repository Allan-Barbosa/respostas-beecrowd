a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
mac = 0
mbc = 0
mab = (a+b+abs(a-b))/2
if(mab == a):
    mac = (a+c+abs(a-c))/2
    print("%d eh o maior" % mac)
else:
    mbc = (c+b+abs(c-b))/2
    print("%d eh o maior" % mbc)
