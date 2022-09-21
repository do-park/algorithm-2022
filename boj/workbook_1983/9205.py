T = int(input())
for t in range(T):
    N = int(input())
    cvs = [list(map(int, input().split())) for _ in range(N + 2)]
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    success = True

    for n in range(N + 2):
        for m in range(N + 2):
            if abs(cvs[n][0] - cvs[m][0]) + abs(cvs[n][1] - cvs[m][1]) <= 1000:
                visited[n][m] = visited[m][n] = 1

    for n in range(N + 2):
        for m in range(N + 2):
            if visited[n][m]:
                for l in range(N + 2):
                    if visited[m][l]:
                        visited[n][l] = visited[l][n] = 1

    print('happy' if visited[0][N + 1] else 'sad')