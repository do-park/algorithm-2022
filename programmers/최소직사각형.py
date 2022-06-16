def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        width = width if min(size) < width else min(size)
        height = height if max(size) < height else max(size)
    return width * height


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133)
