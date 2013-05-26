def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

P = primes(1000000)


def distinct_factor_count(n):
    count, k = 0, n
    for p in P:
        if k == 1 or p > k:
            break
        if k % p == 0:
            count += 1
            while k % p == 0:
                k /= p
    return count


L = []
for n in range(1, 1000000):
    L.append(distinct_factor_count(n))
    if tuple(L[-4:]) == (4, 4, 4, 4):
        print n - 3
        break
