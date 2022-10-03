from collections import deque

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
Q.append([r, c, d])
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
result = 1
count = 0

while Q:
    y, x, dir = Q.popleft()
    dir = dir - 1 if dir > 0 else 3
    ny, nx = y + dys[dir], x + dxs[dir]
    if 0 <= ny < N and 0 <= nx < M and not field[ny][nx] and not visited[ny][nx]:
        visited[ny][nx] = 1
        Q.append([ny, nx, dir])
        result += 1
        count = 0
    else:
        count += 1
        if count > 3:
            ny, nx = y - dys[dir], x - dxs[dir]
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                break
            Q.append([ny, nx, dir])
            count = 0
        else:
            Q.append([y, x, dir])
print(result)