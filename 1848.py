for i in range(3):
    s = 0
    o = 4
    while o != 'caw caw':
        o = input()
        o = o.replace('-', '0')
        o = o.replace('*', '1')
        if o != 'caw caw':
            o = int(o, 2)
            s += o
    print(s)
