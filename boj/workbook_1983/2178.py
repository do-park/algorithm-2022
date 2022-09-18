from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = deque()
Q.append([0, 0])
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while Q:
    y, x = Q.popleft()
    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]
        if 0 <= Y < N and 0 <= X < M and maze[Y][X] and not visited[Y][X]:
            Q.append([Y, X])
            visited[Y][X] = visited[y][x] + 1
print(visited[N-1][M-1])