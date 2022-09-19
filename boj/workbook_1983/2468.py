from collections import deque

N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

result = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for height in range(1, 101):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and ground[i][j] > height:
                Q = deque()
                Q.append([i, j])
                visited[i][j] = 1
                count += 1
                while Q:
                    y, x = Q.popleft()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and ground[ny][nx] > height:
                            Q.append([ny, nx])
                            visited[ny][nx] = 1
            else:
                visited[i][j] = 1
    result = count if count > result else result
    if count == 0:
        break
print(result)
