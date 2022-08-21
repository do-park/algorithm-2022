S = int(input())
answer = 1
while answer*(answer+1) / 2 <= S:
    answer += 1
print(answer - 1)