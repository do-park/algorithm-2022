V = int(input())
votes = list(map(str, input()))
result = 0
for vote in votes:
    result = result +1 if vote == 'A' else result - 1

if result > 0:
    print('A')
elif result == 0:
    print('Tie')
else:
    print('B')