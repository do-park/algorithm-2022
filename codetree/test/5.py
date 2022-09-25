n, k = map(int, input().split())
directions = {'W': [0, -1], 'S': [1, 0], 'N': [-1, 0], 'E': [0, 1]}
visited = [[0]*n for _ in range(n)]
y, x = 0, 0
for i in range(k):
    direction, distance = map(str, input().split())
    dy, dx = directions[direction]
    for j in range(int(distance)):
        y += dy
        x += dx
        visited[y][x] += 1
for v in visited:
    print(*v)