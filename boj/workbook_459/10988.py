text = list(map(str, input()))
answer = 1
for i in range(0, len(text) // 2):
    if text[i] != text[len(text) - i - 1]:
        answer = 0
        break
print(answer)