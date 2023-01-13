N = int(input())
A = list(map(int, input().split()))

isValid = True
result = 0
while isValid:
    for i in range(len(A)):
        if A[i] % 2 == 0:
            if i == len(A) - 1:
                result += 1
                A = list(map(lambda val: val / 2, A))
            continue
        else:
            isValid = False
            break
print(result)
