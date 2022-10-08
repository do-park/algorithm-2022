def comb(array, length_of_result, depth, index):
    if length_of_result == depth:
        print(result)
        return
    for i in range(index, len(array)):
        result[depth] = array[i]
        comb(array, length_of_result, depth + 1, i + 1)


A = [1, 2, 3, 4, 5]
result = [0, 0]
# comb
# 1: comb 돌릴 배열, 2: comb 결과의 길이, 3: 현재의 depth, 4: index
comb(A, 2, 0, 0)