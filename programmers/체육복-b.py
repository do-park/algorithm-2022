def solution(n, lost, reserve):
    students = [1] * n
    for l in lost:
        students[l - 1] -= 1
    for r in reserve:
        students[r - 1] += 1
    answer = 0
    for i in range(n):
        if students[i]:
            students[i] -= 1
            answer += 1
        else:
            if i > 0 and students[i - 1]:
                students[i - 1] -= 1
                answer += 1
            elif i + 1 < n and students[i + 1] == 2:
                students[i + 1] -= 1
                answer += 1
    return answer


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
