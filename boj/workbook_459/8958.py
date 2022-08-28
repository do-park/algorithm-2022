TC = int(input())
for _ in range(TC):
    oxQuiz = list(map(str, input()))
    score, answer = 1, 0
    for i in oxQuiz:
        if i == 'O':
            answer += score
            score += 1
        else:
            score = 1
    print(answer)