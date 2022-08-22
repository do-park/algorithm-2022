T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    X = min(A, B)

    for x in range(X, 0, -1):
        if A % x == 0 and B % x == 0:
            break

    print(A*B//x)
