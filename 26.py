pairs = []
for d in range(1, 1000):
    n = 1
    L = []
    while n:
        L.append(n)
        q, n = divmod(n, d)
        n *= 10
        if n in L:
            pairs.append((L.index(n) - len(L), d))
            break
pairs.sort()
print pairs[0][1]
