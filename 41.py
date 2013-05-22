from math import sqrt
from itertools import permutations

# Here we can see that unless n is 1, 4 or 7 the digits will
# sum to a multiple of 3, and so the number will certainly
# not be prime.

candidates = set()
for i in (1, 4, 7):
    candidates |= set(int("".join(x)) for x in permutations("123456789"[:i]))

primes = set()
for n in candidates:
    if not any(n % i == 0 for i in range(2, int(sqrt(n) + 1))):
        primes.add(n)

print max(primes)
