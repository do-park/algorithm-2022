from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
Q = deque()
Q.append(N)

while Q:
    now = Q.popleft()
    if 0 <= now - 1 <= 100000 and not visited[now - 1]:
        visited[now - 1] = visited[now] + 1
        Q.append(now - 1)
    if 0 <= now + 1 <= 100000 and not visited[now + 1]:
        visited[now + 1] = visited[now] + 1
        Q.append(now + 1)
    if 0 <= now * 2 <= 100000 and not visited[now * 2]:
        visited[now * 2] = visited[now] + 1
        Q.append(now * 2)

print(visited[K] - 1)