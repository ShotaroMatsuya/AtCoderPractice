S = str(input())

results = [False] * (len(S) + 1)
results[0] = True
for i in range(len(S) + 1):
    if i >= 5 and results[i - 5] and S[i - 5 : i] == "dream":
        results[i] = True
    if i >= 7 and results[i - 7] and S[i - 7 : i] == "dreamer":
        results[i] = True
    if i >= 5 and results[i - 5] and S[i - 5 : i] == "erase":
        results[i] = True
    if i >= 6 and results[i - 6] and S[i - 6 : i] == "eraser":
        results[i] = True

print("YES" if results[len(S)] else "NO")
