import sys
sys.stdin = open('20058.txt')

# 출력
# 1. 남아있는 얼음 A[r][c]의 합
# 2. 가장 큰 덩어리가 차지하는 칸의 개수, 덩어리가 없으면 0

# 조건
# 파이어스톰 시전할 때마다 단계 L 결정
# - 격자를 2^L * 2^L 크기의 부분 격자로 나눈다
# - 그 후, 모든 부분 격자를 시계 방향으로 90도 회전
# - 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
# - 이때 (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)
# - 총 Q번의 파이어스톰 시전 이후 [출력] 값 계산해 출력

from collections import deque

N, Q = map(int, input().split())
height = pow(2, N)
ice = [list(map(int, input().split())) for _ in range(height)]
L = list(map(int, input().split()))

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def rotate(r, c, h):
    temp = [[0]*h for _ in range(h)]
    for i in range(h):
        for j in range(h):
            temp[j][h-1-i] = ice[r+i][c+j]
    for i in range(h):
        for j in range(h):
            ice[r+i][c+j] = temp[i][j]


for l in L:
    # - 격자를 2^L * 2^L 크기의 부분 격자로 나눈다
    l_height = pow(2, l)
    # - 그 후, 모든 부분 격자를 시계 방향으로 90도 회전
    for y in range(0, height, l_height):
        for x in range(0, height, l_height):
            rotate(y, x, l_height)

    # - 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    new_ice = [[0]*height for _ in range(height)]
    for y in range(height):
        for x in range(height):
            if ice[y][x] > 0:
                count = 0
                for dy, dx in zip(dys, dxs):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < height and ice[ny][nx] > 0:
                        count += 1
                new_ice[y][x] = ice[y][x] if count > 2 else ice[y][x]-1
    ice = new_ice

# 결과 1
result1 = 0
for i in ice:
    result1 += sum(i)
print(result1)

# 결과 2
result2 = 0
Q = deque()
visited = [[0]*height for _ in range(height)]
for a in range(height):
    for b in range(height):
        size = 0
        if not visited[a][b] and ice[a][b] > 0:
            visited[a][b] = 1
            Q.append((a, b))
            size += 1
        while Q:
            r, c = Q.popleft()
            for dr, dc in zip(dys, dxs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < height and not visited[nr][nc] and ice[nr][nc] > 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = 1
                    size += 1
        result2 = max(result2, size)
print(result2)

