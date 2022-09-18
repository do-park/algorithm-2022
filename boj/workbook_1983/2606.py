N = int(input())
V = int(input())
links = [[0] * N for _ in range(N)]
visited = [0] * N

for _ in range(V):
    C1, C2 = map(int, input().split())
    links[C1 - 1][C2 - 1] = 1
    links[C2 - 1][C1 - 1] = 1

stack = [0]

while True:
    now = stack[-1]
    visited[now] = 1
    stack.pop()
    for n in range(N):
        if links[now][n] and n not in stack and visited[n] == 0:
            stack.append(n)
    if not stack:
        break

print(sum(visited) - 1)