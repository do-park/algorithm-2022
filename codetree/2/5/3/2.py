dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# +1 우회전, -1 좌회전

commands = list(map(str, input()))
x, y = [0, 0]
forward = 0
for command in commands:
    if command == 'R':
        forward = (forward + 1) % 4
    elif command == 'L':
        forward = (forward + 3) % 4
    else:
        x = x + dx[forward]
        y = y + dy[forward]
print(x, y)