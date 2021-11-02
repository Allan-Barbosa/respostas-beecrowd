X = 0
Y = 1
while(X != Y):
    X, Y = input().split(" ")
    X = int(X)
    Y = int(Y)
    if(X > Y):
        print("Decrescente")
    if(X < Y):
        print("Crescente")
