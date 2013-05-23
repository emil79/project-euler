def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

print sum(primes(2000000))
