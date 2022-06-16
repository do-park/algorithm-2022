def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        sqrt = number ** 0.5
        if sqrt == int(sqrt):
            answer -= number
        else:
            answer += number
    return answer


print(solution(13, 17) == 43)
print(solution(24, 27) == 52)
