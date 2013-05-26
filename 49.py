from itertools import permutations, combinations


def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]


P = {p for p in primes(10000) if p > 999}

S = {}
for p in P:
    pp = set()
    for perm in permutations(str(p)):
        q = int(''.join(perm))
        if q in P:
            pp.add(q)
    S[min(pp)] = sorted(pp)

for pp in S.values():
    for triple in combinations(pp, 3):
        # According to docs, triple is sorted correctly
        if triple[0] + triple[2] == 2 * triple[1]:
            if not 1487 in triple:
                print '{}{}{}'.format(*triple)
