def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

P = primes(1000000)
PS = set(P)

candidates = []
for j in range(len(P)):
    t = 0
    for k in range(j, len(P)):
        t += P[k]
        if t >= 1000000:
            break
        if t in PS:
            candidates.append((j - k, t))
print sorted(candidates)[0][1]
