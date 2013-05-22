from math import sqrt
from itertools import product

# For this problem, it makes sense to be clever in choosing
# candidates; we can reduce the number easily to 5460, at which
# point we don't need to be that clever with the primality test.

# The trick is that apart from 2 and 5 we can rule out any numbers
# containing the digits 0, 2, 4, 5, 6, 8.

candidates = {2, 3, 5, 7}
for i in range(2, 7):
    candidates |= set(int("".join(x)) for x in product("1379", repeat=i))

primes = set()
for n in candidates:
    if not any(n % i == 0 for i in range(2, int(sqrt(n) + 1))):
        primes.add(n)

circular_primes = set()
for n in primes:
    s = str(n)
    if all(int(s[i:] + s[:i]) in primes for i in range(1, len(s))):
        circular_primes.add(n)

print len(circular_primes)
