n = float(input())
n = round(n, 2)
if(0 <= n <= 1000000.00):
    n100 = n//100
    n = n-n100*100
    n50 = n//50
    n = n-n50*50
    n20 = n//20
    n = n-n20*20
    n10 = n//10
    n = n-n10*10
    n5 = n//5
    n = n-n5*5
    n2 = n//2
    n = n-n2*2
    m1 = n//1
    n = n-m1*1
    n = round(n, 2)
    m2 = n//0.5
    n = n-m2*0.5
    m2 = round(m2, 2)
    n = round(n, 2)
    m3 = n//0.25
    n = n-m3*0.25
    m3 = round(m3, 2)
    n = round(n, 2)
    m4 = n//0.1
    n = n-m4*0.1
    m4 = round(m4, 2)
    n = round(n, 2)
    m5 = n//0.05
    n = n-m5*0.05
    n = round(n, 2)
    m5 = round(m5, 2)
    m6 = n*100
    print("NOTAS:")
    print("%d nota(s) de R$ 100.00" % n100)
    print("%d nota(s) de R$ 50.00" % n50)
    print("%d nota(s) de R$ 20.00" % n20)
    print("%d nota(s) de R$ 10.00" % n10)
    print("%d nota(s) de R$ 5.00" % n5)
    print("%d nota(s) de R$ 2.00" % n2)
    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00" % m1)
    print("%d moeda(s) de R$ 0.50" % m2)
    print("%d moeda(s) de R$ 0.25" % m3)
    print("%d moeda(s) de R$ 0.10" % m4)
    print("%d moeda(s) de R$ 0.05" % m5)
    print("%d moeda(s) de R$ 0.01" % m6)
