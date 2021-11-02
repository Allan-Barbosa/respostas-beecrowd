t1, t2, t3 = input().split(' ')
t1, t2, t3 = int(t1), int(t2), int(t3)
if t2 < t1 and t3 >= t2 or t2 > t1 and t3 > t2 and t3-t2 >= t2-t1 or t2 < t1 and t3 < t2 and t2-t3 < t1-t2 or t1 == t2 and t3 > t2:
    print(':)')
else:
    print(':(')
