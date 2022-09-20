N = int(input())
X, Y = map(int, input().split())
family = [[-1] * (N + 1) for _ in range(N + 1)]
I = int(input())
for i in range(I):
    A, B = map(int, input().split())
    family[A][B] = 1
    family[B][A] = 1

for n in range(1, N + 1):
    for m in range(1, N + 1):
        if family[n][m] > -1:
            for l in range(1, N + 1):
                if family[m][l] > -1:
                    link = family[n][m] + family[m][l]
                    if family[n][l] == -1 or family[n][l] > link:
                        family[n][l] = link
                        family[l][n] = link
print(family[X][Y])