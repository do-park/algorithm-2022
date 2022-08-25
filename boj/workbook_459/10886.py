N = int(input())
cute = 0
for n in range(N):
    answer = int(input())
    cute = cute + 1 if answer > 0 else cute - 1
print('Junhee is cute!' if cute > 0 else 'Junhee is not cute!')