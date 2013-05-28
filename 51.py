from itertools import combinations


def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

Primes = primes(1000000)


def replace_with_stars(s, positions):
    ns = ""
    for i in range(len(s)):
        ns += "*" if i in positions else s[i]
    return ns


stars = {}
for length in (5, 6):
    for k in range(2, 4):
        for comb in combinations(range(length), k):
            for p in Primes:
                s = str(p)
                if len(s) == length:
                    if len({s[i] for i in comb}) == 1:
                        stars.setdefault(replace_with_stars(s, comb),
                                         []).append(p)

candidates = []
for s, numbers in stars.items():
    candidates.append((len(numbers), numbers[0]))

print sorted(candidates)[-1][1]
