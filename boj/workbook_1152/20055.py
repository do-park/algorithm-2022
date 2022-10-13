import sys
sys.stdin = open('20055.txt')

# 출력: 몇 번째 단계가 진행 중일때 종료되었는지 출력
# 조건
# 1. 로봇은 올리는 위치에만 올릴 수 있다.
# 2. 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
# 3. 로봇은 컨베이어 벨트 위에서 스스로 움직일 수 있다.
# 4. 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
# 5. 로봇을 옮기는 과정
# 5-1. 벨트가 각 칸 위에 있는 로봇과 함께 회전
# 5-2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다. 이동할 수 없다면 가만히 있는다.
# 5-2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 5-3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 5-4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
# 종료되었을 때 몇 번째 단계가 진행 중이었는가
# 가장 처음 수행되는 단계는 1단계

N, K = map(int, input().split())
A = list(map(int, input().split()))
cells = [A[:N], list(reversed(A[N:]))]
robots = [[0]*N for _ in range(2)]


def rotate_belts(belts):
    temp = [[0]*N for _ in range(2)]
    temp[0][0] = belts[1][0]
    for i in range(1, N):
        temp[0][i] = belts[0][i - 1]
    temp[1][N-1] = belts[0][N - 1]
    for i in range(N-1):
        temp[1][i] = belts[1][i + 1]
    return temp


tc = 0
while True:
    tc += 1
    cells, robots = rotate_belts(cells), rotate_belts(robots)
    if robots[0][N-1]:
        robots[0][N-1] = 0
    for n in range(N-2, 0, -1):
        if robots[0][n] and not robots[0][n+1] and cells[0][n+1] > 0:
            robots[0][n], robots[0][n+1] = 0, 1
            cells[0][n+1] -= 1
            if cells[0][n+1] == 0:
                K -= 1
    if robots[0][N-1]:
        robots[0][N-1] = 0
    if cells[0][0] > 0:
        robots[0][0] = 1
        cells[0][0] -= 1
        if cells[0][0] == 0:
            K -= 1

    if K == 0:
        break

print(tc)