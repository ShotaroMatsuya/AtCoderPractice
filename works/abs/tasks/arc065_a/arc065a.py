S = str(input())


def recursive(S):
    a = False
    b = False
    c = False
    d = False
    if S == "":
        return True
    if len(S) >= 5 and S[0:5] == "dream":
        a = recursive(S[5:])
        if len(S) >= 7 and S[0:7] == "dreamer":
            b = recursive(S[7:])

    if len(S) >= 5 and S[0:5] == "erase":
        c = recursive(S[5:])
        if len(S) >= 6 and S[0:6] == "eraser":
            d = recursive(S[6:])

    return a or b or c or d


if recursive(S):
    print("YES")
else:
    print("NO")
