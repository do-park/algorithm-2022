scores = []
for _ in range(5):
    score = int(input())
    scores.append(score if score > 40 else 40)
print(sum(scores) // 5)