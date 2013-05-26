def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return {i for i in L if i > 1}

P = primes(20000)
T = {2 * i * i for i in range(1, 100)}
C = {i for i in range(3, 20000, 2) if not i in P} \
    - {p + t for t in T for p in P}
print min(C)
