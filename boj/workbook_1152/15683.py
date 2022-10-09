import sys
sys.stdin = open('16235.txt')


def watch(depth):
    global result
    if depth == len(cctvs):
        count = 0
        for n in range(N):
            for m in range(M):
                if office[n][m] != 6 and not visited[n][m]:
                    count += 1
        result = min(result, count)
        return
    y, x, cctv = cctvs[depth]
    for cctv_check in cctv_checks[cctv]:
        for check in cctv_check:
            ny, nx = y, x
            while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
                visited[ny][nx] += 1
                ny, nx = ny + dys[check], nx + dxs[check]
        watch(depth + 1)
        for check in cctv_check:
            ny, nx = y, x
            while 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
                visited[ny][nx] -= 1
                ny, nx = ny + dys[check], nx + dxs[check]


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cctvs = []

for n in range(N):
    for m in range(M):
        if 1 <= office[n][m] <= 5:
            cctvs.append((n, m, office[n][m] - 1))

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
cctv_checks = [[[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]]
result = N*M
watch(0)
print(result)

