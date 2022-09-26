from collections import deque

F, S, G, U, D = map(int, input().split())
# 총 F층의 건물, 목적지 G층, 현재 S층, U층만큼 위로 이동, D층만큼 아래로 이동
building = [0] * (F + 1)
Q = deque()
Q.append(S)
building[S] = 1
while Q:
    now = Q.popleft()
    next_up = now + U
    if next_up <= F and not building[next_up]:
        building[next_up] = building[now] + 1
        Q.append(next_up)
    next_down = now - D
    if next_down > 0 and not building[next_down]:
        building[next_down] = building[now] + 1
        Q.append(next_down)
print(building[G] - 1 if building[G] else 'use the stairs')