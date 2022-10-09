from collections import deque

dys = [-1, -1, -1, 0, 0, 1, 1, 1]
dxs = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
field = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for i in range(N)] for j in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for k in range(K):
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                temp_Q = deque()
                nutrition = 0
                while trees[r][c]:
                    year = trees[r][c].popleft()
                    if field[r][c] >= year:
                        field[r][c] -= year
                        temp_Q.append(year + 1)
                    else:
                        nutrition += year//2
                trees[r][c] = temp_Q
                field[r][c] += nutrition
    for r in range(N):
        for c in range(N):
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for dy, dx in zip(dys, dxs):
                        ny, nx = r + dy, c + dx
                        if 0 <= ny < N and 0 <= nx < N:
                            trees[ny][nx].appendleft(1)
            field[r][c] += s2d2[r][c]

result = 0
for r in range(N):
    for c in range(N):
        result += len(trees[r][c])
print(result)