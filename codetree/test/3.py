n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
for i in range(r):
    for j in range(c):
        result[i][j] = 0 if result[i][j] < result[r-1][c-1] else result[i][j]
for row in result:
    print(*row)