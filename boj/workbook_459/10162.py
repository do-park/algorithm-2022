T = int(input())
A, B, C = 0, 0, 0

if T // 300:
    A += T // 300
    T = 300 * A
if T // 60:
    B += T // 60
    T -= 60 * B
if T // 10:
    C += T // 10
    T -= 10 * C
print(f'{A} {B} {C}' if T == 0 else -1)