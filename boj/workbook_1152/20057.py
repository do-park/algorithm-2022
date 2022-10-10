import sys
sys.stdin = open('20057.txt')

# 출력: 격자 밖으로 나간 모래의 양
# N*N인 격자로 나뉜 모래밭, (r, c)는 r행 c열, A[r][c]는 (r,c)에 있는 모래의 양
# 토네이도를 시전하면 가운데칸부터 토네이도 이동

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
y, x = N//2, N//2
delta = -1
count = 1
result = 0

torn_r = [
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],    # left
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],      # down
    [1, -1, 2, -2, 0, 1, -1, 1, -1],    # right
    [1, 1, 0, 0, -2, 0, 0, -1, -1]      # up
]
torn_c = [
    [1, 1, 0, 0, -2, 0, 0, -1, -1],     # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],      # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1]     # up
]
rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

drs = [0, 1, 0, -1]
dcs = [-1, 0, 1, 0]


def tornado(r, c, dir):
    global result
    total_sand, left_sand = A[r][c], A[r][c]
    for s in range(9):
        nr = r + torn_r[dir][s]
        nc = c + torn_c[dir][s]
        blown_sand = total_sand * rate[s] // 100
        if 0 <= nr < N and 0 <= nc < N:
            A[nr][nc] += blown_sand
        else:
            result += blown_sand
        left_sand -= blown_sand
    nr, nc = r + drs[dir], c + dcs[dir]
    if 0 <= nr < N and 0 <= nc < N:
        A[nr][nc] += left_sand
    else:
        result += left_sand


for i in range(1, N*2):
    for j in range(count):
        if i % 2 == 1:
            x = x + delta
            tornado(y, x, 0 if delta < 0 else 2)
        else:
            y = y + delta
            tornado(y, x, 1 if delta > 0 else 3)
        if (x, y) == (0, 0):
            break
    if i % 2 == 0:
        count += 1
    else:
        delta *= -1
print(result)