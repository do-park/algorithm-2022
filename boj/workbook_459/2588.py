A = int(input())
B = int(input())
temp = B
while temp:
    print(A*(temp%10))
    temp = temp//10
print(A*B)