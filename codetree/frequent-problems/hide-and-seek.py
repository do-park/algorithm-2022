import sys

sys.stdin = open('hide-and-seek.txt')

# 출력: 술래가 k번의 턴 동안 얻게되는 총 점수

# 입력
# N*N 크기의 격자 / M명의 도망자 / H그루의 나무 / K번 동안 턴 반복
from collections import deque

N, M, H, K = map(int, input().split())
runners = deque()
for m in range(M):
    y, x, d = map(int, input().split())
    runners.append([y - 1, x - 1, d])
# 도망자의 위치 (y, x)와 d가 공백을 사이에 두고 주어짐
# (d=1인 경우 좌우, d=2인 경우 상하 / 오른쪽부터, 아래쪽부터 이동)
# 나무의 위치 (y, x)가 공백을 두고 주어짐
trees = [[0] * N for _ in range(N)]
for h in range(H):
    y, x = map(int, input().split())
    trees[y - 1][x - 1] = 1

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 오른쪽 아래 왼쪽
catcher = [N // 2, N // 2, 0]
catcher_rotate_direction = 1  # 1일때 달팽이, -1일때 반대
catcher_move_list_index = 0  # catcher_move_list 에서 몇 번째에 위치했는지
catcher_move_list_index_count = 0  # catcher_move_list_index 내부에서 몇 번째인지
catcher_move_list = []
for i in range(1, N):
    catcher_move_list.append(i)
    catcher_move_list.append(i)
catcher_move_list.append(N - 1)
catcher_move_count = 0
result = 0


# 도망자가 이동
# 술래와의 거리가 3 이하인 도망자만
# 거리 계산은 |y1-y2| + |x1-x2|
# 현재 바라보고 있는 방향으로 1칸 이동
# 격자를 벗어나지 않는 경우
# 술래가 해당 칸에 있으면 움직이지 않는다.
# 그렇지 않다면 이동
# 격자를 벗어나는 경우
# 방향 회전
def move_runners():
    temp = deque()
    while runners:
        y, x, d = runners.popleft()
        distance = abs(catcher[0] - y) + abs(catcher[1] - x)
        if distance > 3:
            temp.append([y, x, d])
        else:
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) == (catcher[0], catcher[1]):
                    temp.append([y, x, d])
                else:
                    temp.append([ny, nx, d])
            else:
                d = (d + 2) % 4
                dy, dx = directions[d]
                ny, nx = y + dy, x + dx
                if (ny, nx) == (catcher[0], catcher[1]):
                    temp.append([y, x, d])
                else:
                    temp.append([ny, nx, d])
    return temp


# 술래가 이동
# 가운데에서부터 달팽이 모양으로 이동
# 이동이 끝나면 반대로 다시 돌아서 옴
# 이동 방향이 틀어지는 지점이라면 바로 방향을 틀어준다.
# 정중앙과 (0, 0)에서도 바로 회전해야 한다.
def move_catcher():
    global catcher_move_list_index, catcher_move_list_index_count, catcher_rotate_direction
    dy, dx = directions[catcher[2]]
    catcher[0], catcher[1] = catcher[0] + dy, catcher[1] + dx
    catcher_move_list_index_count += 1
    if catcher_move_list[catcher_move_list_index] == catcher_move_list_index_count:
        if (catcher_move_list_index + 1 == len(catcher_move_list) and catcher_rotate_direction > 0)\
                or (catcher_move_list_index == 0 and catcher_rotate_direction < 0):
            catcher_rotate_direction *= -1
            catcher_move_list_index_count = 0
            catcher[2] = (catcher[2] + 2) % 4
        else:
            catcher_move_list_index += catcher_rotate_direction
            catcher_move_list_index_count = 0
            catcher[2] = (catcher[2] + 1) % 4 if catcher_rotate_direction > 0 else (4 + catcher[2] - 1) % 4


# 술래잡기
# 술래가 바라보고 있는 방향 기준으로 현재 칸 포함해 3칸
# 나무가 있는 칸에 있으면 잡히지 않는다.
# 잡힌 도망자는 맵에서 사라지게 된다.
# 현재 턴 횟수 * 현재 턴에서 잡힌 도망자의 수만큼 점수를 얻는다.
def seek_runners(turn):
    global runners
    dy, dx = directions[catcher[2]]
    count = 0
    for i in range(3):
        ny, nx = catcher[0] + dy * i, catcher[1] + dx * i
        if 0 <= ny < N and 0 <= nx < N and not trees[ny][nx]:
            temp = deque()
            while runners:
                r, c, d = runners.popleft()
                if (r, c) == (ny, nx):
                    count += 1
                else:
                    temp.append([r, c, d])
            runners = temp
    return turn * count


for k in range(1, K + 1):
    runners = move_runners()
    move_catcher()
    result += seek_runners(k)
    if len(runners) == 0:
        break
print(result)
