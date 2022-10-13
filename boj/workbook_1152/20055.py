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

from collections import deque

N, K = map(int, input().split())
cells = deque(map(int, input().split()))
robots = deque([0]*N)

tc = 0
while True:
    tc += 1
    cells.rotate(1)
    robots.rotate(1)
    for n in range(N-1, -1, -1):
        if robots[n]:
            if n == N-1:
                robots[n] = 0
            elif not robots[n+1] and cells[n+1]:
                robots[n], robots[n+1] = 0, 1
                cells[n+1] -= 1
                if n+1 == N-1:
                    robots[n+1] = 0
    if cells[0]:
        robots[0] = 1
        cells[0] -= 1
    count = 0
    for cell in cells:
        if cell == 0:
            count += 1
    if count >= K:
        break
print(tc)