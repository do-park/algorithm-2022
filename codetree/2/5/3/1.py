n = int(input())
directions = {'W': [0, -1], 'S': [-1, 0], 'N': [1, 0], 'E': [0, 1]}
y, x = 0, 0
for i in range(n):
    direction, distance = map(str, input().split())
    dy, dx = directions[direction]
    y += dy * int(distance)
    x += dx * int(distance)
print(x, y)