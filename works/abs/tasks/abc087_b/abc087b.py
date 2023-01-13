A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i in range(A + 1):
    SUM = 0
    a_sum = 0
    b_sum = 0
    c_sum = 0
    a_sum = i * 500
    SUM = a_sum
    if SUM == X:
        count += 1
    if SUM >= X:
        break
    for j in range(B + 1):
        b_sum = j * 100
        SUM = a_sum + b_sum
        if SUM == X:
            count += 1
        if SUM >= X:
            break
        for k in range(C + 1):
            c_sum = k * 50
            SUM = a_sum + b_sum + c_sum
            if SUM == X:
                count += 1
            if SUM >= X:
                break

print(count)
