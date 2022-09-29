from collections import deque

dzs = [-1, 1, 0, 0, 0, 0]
dys = [0, 0, -1, 1, 0, 0]
dxs = [0, 0, 0, 0, -1, 1]
N, M, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for m in range(M)] for h in range(H)]
unripe_tomatoes = 0
Q = deque()

for n in range(N):
    for m in range(M):
        for h in range(H):
            if tomatoes[h][m][n] == 1:
                Q.append([h, m, n])
            elif tomatoes[h][m][n] == 0:
                unripe_tomatoes += 1

result = 0
while unripe_tomatoes > 0 and len(Q) > 0:
    temp_Q = deque()
    while Q:
        [z, y, x] = Q.popleft()
        for dz, dy, dx in zip(dzs, dys, dxs):
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N and tomatoes[nz][ny][nx] == 0:
                temp_Q.append([nz, ny, nx])
                tomatoes[nz][ny][nx] = 1
                unripe_tomatoes -= 1
    Q = temp_Q
    result += 1

print(result if unripe_tomatoes == 0 else -1)