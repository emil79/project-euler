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

L = primes(110000)  # Takes about a minute
print L[10000]
