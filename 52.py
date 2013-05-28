for length in range(1, 7):
    for i in range(10 ** (length - 1), 10 ** length / 6):
        s = {tuple(sorted(x for x in str(i * m))) for m in range(2, 7)}
        if len(s) == 1:
            print i
            break
