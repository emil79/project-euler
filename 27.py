# Reused function from my Cython talk
# http://skillsmatter.com/podcast/java-jee/adventures-with-cython


def primes(n):
    L = range(n)
    for i in range(n):
        if L[i] > 1:
            for j in range(i + 1, n):
                if j % i == 0:
                    L[j] = 0
    return [i for i in L if i > 1]

# Not sure if 10000 is high enough - but seems so. Should check!
P = set(primes(10000))  # Turning into a set gives 10x speed increase

candidates = []
# Simple optimization: b should be prime, and so should 1 + a + b
for b in primes(1000):
    for a in range(-999, 1000, 1):
        if 1 + a + b in P:
            n = 0
            while n ** 2 + a * n + b in P:
                n += 1
            if n >= 39:  # From the question, we know we can at least get 40
                candidates.append((n, a, b))

n, a, b = sorted(candidates)[-1]
print a * b
