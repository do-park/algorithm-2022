N = int(input())
while N != -1:
    divisor = []
    for n in range(1, N-1):
        if N % n == 0:
            divisor.append(n)
    if sum(divisor) == N:
        print(f'{N} = ', end="")
        print(' + '.join(map(str, divisor)))
    else:
        print(f"{N} is NOT perfect.")
    N = int(input())