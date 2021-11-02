x, di = input().split(" ")
hi, mi, si = input().split(":")
y, df = input().split(" ")
di = int(di)
df = int(df)
hf, mf, sf = input().split(":")
hi, mi, si = int(hi), int(mi), int(si)
hf, mf, sf = int(hf), int(mf), int(sf)
s = 0
m = 0
h = 0
t = 0
d = 0
ti = (hi*60*60)+(mi*60)+si
tf = (hf*60*60)+(mf*60)+sf
if(tf >= ti):
    d = df-di
if(tf < ti):
    d = df-(di+1)
if(tf > ti):
    t = tf-ti
    h = (t//60)//60
    t = t-(h*60*60)
    m = t//60
    t = t-m*60
    s = t
if(tf < ti):
    tf += 24*60*60
    t = tf-ti
    h = (t//60)//60
    t = t-(h*60*60)
    m = t//60
    t = t-m*60
    s = t
print("%d dia(s)" % d)
print("%d hora(s)" % h)
print("%d minuto(s)" % m)
print("%d segundo(s)" % s)
