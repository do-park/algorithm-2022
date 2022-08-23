A, B = map(int, input().split())
while A + B != 0:
    print('Yes' if A > B else 'No')
    A, B = map(int, input().split())