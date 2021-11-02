n1, n2, n3, n4 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n5 = 0
m = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)
print("Media: %.1f" % m)
if(m >= 7):
    print("Aluno aprovado.")
else:
    if(m < 5):
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        n5 = float(input())
        print("Nota do exame: %.1f" % n5)
        mf = (m+n5)/2
        if(m >= 5):
            print("Aluno aprovado.")
            print("Media final: %.1f" % mf)
        else:
            print("Aluno reprovado.")
            print("Media final: %.1f" % mf)
