import sys
sys.stdin = open('21610.txt')

# 출력: M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양

# 입력
N, M = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(M)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


# 조건
# 1. 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 2. 구름은 M번 이동하며, 이동 명령은 방향 d와 거리 s로 이루어져 있다.
# - 1. 모든 구름이 d 방향으로 s칸 이동
# - 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
# - 3. 구름이 모두 사라진다.
# - 4. 2에서 물이 증가한 칸 (r, c)와 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 증가한다.
# - 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
# 3. 방향은 총 8개

# 조건 3
drs = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dcs = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for cmd in cmds:
    direction, distance = cmd
    moved_clouds = []
    new_clouds = []
    # 2-1. 모든 구름이 d방향으로 s칸 이동
    # 2-2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
    for cloud in clouds:
        r, c = cloud
        nr, nc = (N + r + drs[direction]*distance) % N, (N + c + dcs[direction]*distance) % N
        moved_clouds.append((nr, nc))
        water[nr][nc] += 1
    # 2-4. 2에서 물이 증가한 칸 (r, c)와 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 증가한다.
    for cloud in moved_clouds:
        r, c = cloud
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and water[nr][nc] > 0:
                water[r][c] += 1
    # 2-5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(N):
        for j in range(N):
            if water[i][j] >= 2 and (i, j) not in moved_clouds:
                new_clouds.append((i, j))
                water[i][j] -= 2
    clouds = new_clouds

result = 0
for w in water:
    result += sum(w)
print(result)

