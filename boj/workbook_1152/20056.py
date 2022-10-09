import sys
sys.stdin = open('20056.txt')

# 출력: 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼의 질량의 합
# 조건
# 1. N * N 격자에 파이어볼 M개
# 2. N 다음은 1번으로 연결되어 있다.
# 3. 파이어볼의 방향 위에서부터 시계방향으로 0~7
# 4. 상어가 이동 명령 시 방향 d로 속력 s만큼 이동
# 5. 이동이 끝나고 2개 이상의 파이어볼이 있는 경우
# - 1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
# - 2. 파이어볼은 4개로 나누어진다.
# - 3. 파이어볼의 질량, 속력, 방향은
#       질량: 합쳐진 파이어볼의 질량의 합 / 5
#       속력: 합쳐진 파이어볼의 속력의 합 / 합쳐진 파이어볼의 개수
#       합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수이면 방향은 0, 2, 4, 6
#       그렇지 않으면 1, 3, 57
#       질량이 0인 파이어볼은 소멸된다.
# 파이어볼 스펙: 위치 (r, c) 질량 m, 속력 s, 방향 d

from collections import deque


# 조건 3 처리
dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
fields = [[deque() for i in range(N)] for j in range(N)]
for fireball in range(M):
    r, c, m, s, d = map(int, input().split())
    fields[r-1][c-1].append([m, s, d])

for k in range(K):
    temp_fields = [[deque() for i in range(N)] for j in range(N)]
    # 파이어볼 이동
    for y in range(N):
        for x in range(N):
            while fields[y][x]:
                m, s, d = fields[y][x].popleft()
                # 조건 2 처리
                ny, nx = (y + dys[d]*s + N) % N, (x + dxs[d]*s + N) % N
                temp_fields[ny][nx].append([m, s, d])
    # 조건 5 처리
    for y in range(N):
        for x in range(N):
            if len(temp_fields[y][x]) > 1:
                count = len(temp_fields[y][x])
                total_m, total_s, evens, odds = 0, 0, 0, 0
                while temp_fields[y][x]:
                    fireball = temp_fields[y][x].popleft()
                    total_m += fireball[0]
                    total_s += fireball[1]
                    if fireball[2] % 2 == 0:
                        evens += 1
                    else:
                        odds += 1
                if total_m//5 > 0:
                    if not evens or not odds:
                        for d in [0, 2, 4, 6]:
                            temp_fields[y][x].append([total_m//5, total_s//count, d])
                    else:
                        for d in [1, 3, 5, 7]:
                            temp_fields[y][x].append([total_m//5, total_s//count, d])
    fields = temp_fields

result = 0
for field in fields:
    for fireballs in field:
        for fireball in fireballs:
            result += fireball[0]
print(result)