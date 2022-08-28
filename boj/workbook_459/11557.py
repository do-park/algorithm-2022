T = int(input())
for t in range(T):
    university, alcohol = [], []
    N = int(input())
    for n in range(N):
        U, A = map(str, input().split())
        university.append(U)
        alcohol.append(int(A))
    print(university[alcohol.index(max(alcohol))])