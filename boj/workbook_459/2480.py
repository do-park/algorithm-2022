dices = list(map(int, input().split()))
answer = 0

for eye in dices:
    if dices.count(eye) == 3:
        answer = 10000 + eye*1000
        break
    elif dices.count(eye) == 2:
        answer = 1000 + eye*100
        break
print(answer if answer else max(dices)*100)