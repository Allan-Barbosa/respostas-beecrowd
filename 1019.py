n = int(input())
h = n//3600
m = (n % 3600)//60
s = n % 60
h = str(h)
m = str(m)
s = str(s)
print(h+":"+m+":"+s)
