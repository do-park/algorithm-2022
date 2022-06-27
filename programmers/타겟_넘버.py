from collections import deque


def solution(numbers, target):
    que = deque([0])
    for number in numbers:
        sub_que = deque()
        for b in que:
            sub_que.append(b+number)
            sub_que.append(b-number)
        que = sub_que
    return que.count(target)


print(solution([1, 1, 1, 1, 1], 3) == 5)
print(solution([4, 1, 2, 1], 4) == 2)
