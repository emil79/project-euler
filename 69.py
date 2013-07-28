def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]


# To speed things up (quite considerably, actually), we use a cache.
# This could be implemented as a memoization decorator. We preload
# the cache with the primes, as that seems to help quite a lot.

P = primes(1000000)
cache = {1: []}
for p in P:
    cache[p] = [p]


def prime_factorization(n):
    if n in cache:
        return cache[n]
    for p in P:
        if n % p == 0:
            factors = [p] + prime_factorization(n / p)
            cache[n] = factors
            return factors


def totient(n):
    numer, denom = n, 1
    for p in set(prime_factorization(n)):
        numer *= p - 1
        denom *= p
    return numer / denom


pairs = []
for n in range(1, 1000000):
    pairs.append((n * -1.0 / totient(n), n))

print sorted(pairs)[0][1]
