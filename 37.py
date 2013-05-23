def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

P = set(primes(1000000))

truncatable_primes = set()
for p in P:
    s = str(p)
    if all(int(s[:i]) in P and int(s[-i:]) in P for i in range(1, len(s))):
        truncatable_primes.add(p)

print sum(truncatable_primes - {2, 3, 5, 7})
