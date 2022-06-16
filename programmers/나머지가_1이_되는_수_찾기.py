def solution(n):
    for answer in range(1, n):
        if n % answer == 1:
            return answer


print(solution(10) == 3)
print(solution(12) == 11)
