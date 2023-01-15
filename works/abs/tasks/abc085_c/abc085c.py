N, Y = map(int, input().split())


def otoshidama(N, Y):
    for i in range(N + 1):
        SUM = i * 10000
        if SUM > Y:
            break
        if SUM == Y and N == i:
            return print("{} {} {}".format(i, 0, 0))
        for j in range(N - i + 1):
            SUM = i * 10000 + j * 5000 + (N - i - j) * 1000
            if SUM == Y:
                return print("{} {} {}".format(i, j, (N - i - j)))

    return print("{} {} {}".format(-1, -1, -1))


otoshidama(N, Y)
