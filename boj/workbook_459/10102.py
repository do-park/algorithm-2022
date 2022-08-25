V = int(input())
votes = list(map(str, input()))
A, B = votes.count('A'), votes.count('B')
if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')