T = int(input())
A, B, C = 0, 0, 0

if T % 10:
    print(-1)
else:
    A = T // 300
    T = T % 300
    B = T // 60
    T = T % 60
    C = T // 10
    T = T % 10
    print(f'{A} {B} {C}')