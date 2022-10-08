def perm(array, length_of_result, depth):
    if length_of_result == depth:
        print(result)
        return
    for number in array:
        if number not in result:
            result[depth] = number
            perm(array, length_of_result, depth + 1)
            result[depth] = 0


def perm_with_visited(array, length_of_result, depth):
    if length_of_result == depth:
        print(result)
        return
    for index in range(len(array)):
        if not visited[index]:
            result[depth] = array[index]
            visited[index] = 1
            perm(array, length_of_result, depth + 1)
            visited[index] = 0


A = [1, 2, 3, 4, 5]
visited = [0, 0, 0, 0, 0]
result = [0, 0, 0]
perm(A, 3, 0)
print('=================================')
perm_with_visited(A, 3, 0)