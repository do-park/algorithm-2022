from collections import deque


dzs = [-1, 1, 0, 0, 0, 0]
dys = [0, 0, -1, 1, 0, 0]
dxs = [0, 0, 0, 0, -1, 1]
N, M, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for m in range(M)] for h in range(H)]
# 1. 전체 맵 돌면서 익은 토마토가 있는지 확인 후 Q에 넣기 (시작 지점)
#   - 안 익은 토마토의 개수도 함께 세자
# 2. 익은 토마토들 각각에 대해 BFS 돌리면서 count 세기
# 3. Q가 비었을 때 종료
# 4. 익지 않은 토마토 (0이 있는 경우) 가 있는 경우 -1 출력, 아닌 경우 count 출력




for dz, dy, dx in zip(dzs, dys, dxs):
    print(dz, dy, dx)