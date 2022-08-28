T = int(input())
for t in range(T):
    score = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        score += Y - K
    if score == 0:
        print('Draw')
    else:
        print('Yonsei' if score > 0 else 'Korea')