i = 0
j1 = 1
j2 = 2
j3 = 3
while(i <= 2):
    if(i == int(i) or i == 2):
        print("I=%d" % i, "J=%d" % j1)
        print("I=%d" % i, "J=%d" % j2)
        print("I=%d" % i, "J=%d" % j3)
    if(i != int(i)):
        print("I=%.1f" % i, "J=%.1f" % j1)
        print("I=%.1f" % i, "J=%.1f" % j2)
        print("I=%.1f" % i, "J=%.1f" % j3)
    i += 0.2
    j1 += 0.2
    j1 = round(j1, 2)
    j2 += 0.2
    j3 += 0.2
    i = round(i, 1)
