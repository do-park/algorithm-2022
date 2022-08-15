A, B = map(int, input().split())
C = int(input())
M = (B+C)%60
H = (A+(B+C)//60)%24
print(f'{H} {M}')