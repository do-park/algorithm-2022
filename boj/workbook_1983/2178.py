def BFS(maze, i, j, N, M):
    visited = []
    q = [[i, j]]
    distance = [[0] * M for _ in range(N)]
    distance[0][0] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        [i, j] = q.pop(0)
        visited.append([i, j])

        for d in range(4):
            Y = dy[d] + i
            X = dx[d] + j

            if 0 <= X < M and 0 <= Y < N and maze[Y][X] and [Y, X] not in visited and [Y, X] not in q:
                q.append([Y, X])
                distance[Y][X] = distance[i][j] + 1

    return distance[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

print(BFS(maze, 0, 0, N, M))