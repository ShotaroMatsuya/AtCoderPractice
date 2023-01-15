N = int(input())

S = list(int(input()) for i in range(N))

layer_count = 1
list.sort(S)
current = S[0]
for i in range(1, len(S)):
    if current < S[i]:
        layer_count += 1
    current = S[i]

print(layer_count)
