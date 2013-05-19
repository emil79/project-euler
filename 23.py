from itertools import combinations_with_replacement


def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

abundant_numbers = set()
for i in range(28124):
    if sum_of_proper_divisors(i) > i:
        abundant_numbers.add(i)

sums = set()
for a, b in combinations_with_replacement(abundant_numbers, 2):
    sums.add(a + b)

total = 0
for i in range(1, 28124):
    if not i in sums:
        total += i
print total
