N = int(input())
scoreA, scoreB = 100, 100
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        scoreB -= A
    elif A < B:
        scoreA -= B
print(scoreA)
print(scoreB)