A, B, C = map(int, input().split())
D = int(input())
seconds = A*3600 + B*60 + C + D

print((seconds//3600)%24, (seconds%3600)//60, seconds%60)