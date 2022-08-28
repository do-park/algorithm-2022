N = int(input())
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
for _ in range(N):
    X, Y = map(int, input().split())
    if X > 0:
        if Y > 0:
            Q1 += 1
        elif Y < 0:
            Q4 += 1
        else:
            AXIS += 1
    elif X < 0:
        if Y > 0:
            Q2 += 1
        elif Y < 0:
            Q3 += 1
        else: AXIS += 1
    else:
        AXIS += 1
print('Q1: ' + str(Q1))
print('Q2: ' + str(Q2))
print('Q3: ' + str(Q3))
print('Q4: ' + str(Q4))
print('AXIS: ' + str(AXIS))