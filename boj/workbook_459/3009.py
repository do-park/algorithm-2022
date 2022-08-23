X = {}
Y = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x not in X:
        X[x] = 1
    else:
        X[x] += 1
    if y not in Y:
        Y[y] = 1
    else:
        Y[y] += 1

answerX = 0
answerY = 0
for key, val in X.items():
    if val == 1:
        answerX = key
        break
for key, val in Y.items():
    if val == 1:
        answerY = key
        break
print(answerX, answerY)