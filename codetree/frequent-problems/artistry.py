import sys
sys.stdin = open('artistry.txt')

# 출력: 초기 예술 점수, 1회전 후 예술 점수, 2회전 후 예술 점수, 3회전 후 예술 점수의 합

from collections import deque

N = int(input())
picture = [list(map(int, input().split())) for _ in range(N)]
half_N = N // 2


def calc_artistry(array):
    # 동일한 숫자가 상하좌우 인접해 있는 경우를 동일한 그룹이라 본다.
    # 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의
    # 그룹 a - b의 조화로움은
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) * 그룹 a를 이루고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값 * 그룹 a와 b가 서로 맞닿아 있는 변의 수
    group_number = 1
    Q = deque()
    grouped_picture = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not grouped_picture[i][j]:
                group_value = array[i][j]
                Q.append((i, j))
                grouped_picture[i][j] = group_number
                while Q:
                    y, x = Q.popleft()
                    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not grouped_picture[ny][nx] and array[ny][nx] == group_value:
                            Q.append((ny, nx))
                            grouped_picture[ny][nx] = group_number
                group_number += 1
    group_infos = []
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group_number, group_value, group_size = grouped_picture[i][j], array[i][j], 1
                near_groups = dict()
                Q.append((i, j))
                visited[i][j] = 1
                while Q:
                    y, x = Q.popleft()
                    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                            if grouped_picture[ny][nx] == group_number:
                                group_size += 1
                                Q.append((ny, nx))
                                visited[ny][nx] = 1
                                grouped_picture[ny][nx] = group_number
                            else:
                                if grouped_picture[ny][nx] in near_groups:
                                    near_groups[grouped_picture[ny][nx]] += 1
                                else:
                                    near_groups[grouped_picture[ny][nx]] = 1
                group_infos.append([group_number, group_value, group_size, near_groups])
    score = 0
    for group_number, group_value, group_size, near_group in group_infos:
        for key, value in near_group.items():
            another_number, another_value, another_size, another = group_infos[key -1]
            score += (group_size + another_size) * group_value * another_value * value
    return score


def rotate_pictrue(array):
    # 정중을 기준으로 두 선을 그어 만들어지는 십자 모양과 그 외 부분으로 나뉘어 진행
    # 십자 모양의 경우 통째로 반시계 방향으로 90도 회전
    # 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90도씩 회전
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        temp[i][half_N] = array[half_N][N-i-1]
        temp[half_N][i] = array[i][half_N]

    for i in range(half_N):
        for j in range(half_N):
            temp[i][j] = array[half_N-j-1][i]
            temp[half_N+1+i][j] = array[N-j-1][i]
            temp[i][half_N+j+1] = array[half_N-1-j][half_N+1+i]
            temp[half_N+1+i][half_N+j+1] = array[N-1-j][half_N+i+1]
    return temp


result = 0
for r in range(4):
    result += calc_artistry(picture)
    picture = rotate_pictrue(picture)
print(result)