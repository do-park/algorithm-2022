N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = []
color = 0
for n in range(N):
    for m in range(N):
        if maze[n][m] == 1 and visited[n][m] == 0:
            color += 1
            stack = [(n, m)]
            count = 1
            visited[n][m] = color
            while stack:
                y, x = stack.pop()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        if not visited[ny][nx]:
                            if maze[ny][nx]:
                                visited[ny][nx] = color
                                stack.append([ny, nx])
                                count += 1
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)