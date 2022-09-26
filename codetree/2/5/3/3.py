n = int(input())
fields = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
result = 0
for i in range(n):
    for j in range(n):
        total = 0
        for dy, dx in zip(dys, dxs):
            y, x = i + dy, j + dx
            if 0 <= y < n and 0 <= x < n and fields[y][x] == 1:
                total += 1
        if total >= 3:
            result += 1
print(result)