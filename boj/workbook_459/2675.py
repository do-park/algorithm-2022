T = int(input())
for t in range(1, T+1):
    R, S = map(str, input().split())
    R = int(R)
    result = ''
    for s in S:
        result += s * R
    print(result)