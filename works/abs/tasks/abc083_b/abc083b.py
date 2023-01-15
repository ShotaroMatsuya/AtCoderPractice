N, A, B = map(int, input().split())

num_arr = []

sum = 0

for i in range(1, N + 1):
    num_arr.append(i)

for i in range(len(num_arr)):
    current_num = num_arr[i]
    count = 0
    for i in range(len(str(current_num))):
        count += int(str(current_num)[i])
    if A <= count and B >= count:
        sum += current_num

print(sum)
