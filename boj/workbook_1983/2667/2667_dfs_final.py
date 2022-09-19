def dfs(y, x, size):
    global count
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < size and 0 <= nx < size:
            if not visited[ny][nx]:
                if maze[ny][nx]:
                    visited[ny][nx] = color
                    count += 1
                    dfs(ny, nx, size)


N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

result = []
color = 0
for n in range(N):
    for m in range(N):
        if maze[n][m] == 1 and visited[n][m] == 0:
            color += 1
            count = 1
            visited[n][m] = color
            dfs(n, m, N)
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)