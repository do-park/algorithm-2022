import sys
sys.stdin = open('20058.txt')

N, Q = map(int, input().split())
height = pow(2, N)
ice = [list(map(int, input().split())) for _ in range(height)]
L = list(map(int, input().split()))

temp = [[0]*height for _ in range(height)]
for i in range(height):
    for j in range(height):
        temp[j][height-1-i] = ice[i][j]

for i in ice:
    print(i)

print()

for t in temp:
    print(t)