from itertools import combinations
from networkx import Graph, find_cliques

# Most of the time (about 60 seconds) is spent
# in the primes function. Not sure if it's cheating
# to use networkx...


def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(2 * i, n, i):
                L[j] = 0
    return [i for i in L if i > 1]

Primes = set(primes(100000000))

G = Graph()
for p, q in combinations(sorted(p for p in Primes if p < 10000), 2):
    s, t = str(p), str(q)
    if int(s + t) in Primes and int(t + s) in Primes:
        G.add_edge(p, q)

print min({sum(C) for C in find_cliques(G) if len(C) == 5})
