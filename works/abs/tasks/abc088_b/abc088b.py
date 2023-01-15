N = int(input())
A = list(map(int, input().split()))

list.sort(A, reverse=True)

Alice = 0
Bob = 0
for i in range(len(A)):
    if i % 2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]


print(Alice - Bob)
