from itertools import permutations

primes = (2, 3, 5, 7, 11, 13, 17)

total = 0
for perm in permutations('0123456789'):
    s = "".join(perm)
    if all(int(s[1 + i: 1 + i + 3]) % p == 0
           for i, p in enumerate(primes)):
        total += int(s)
print total
