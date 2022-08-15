T = int(input())
for t in range(1, T+1):
    string = list(map(str, input().split()))
    result = float(string[0])
    for i in range(1, len(string)):
        if string[i] == '@':
            result *= 3
        elif string[i] == '%':
            result += 5
        else:
            result -= 7
    print('%0.2f' % result)
