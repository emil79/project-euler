def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

amicable_numbers = set()
for a in range(1, 10000):
    b = sum_of_proper_divisors(a)
    if a != b and a == sum_of_proper_divisors(b):
        amicable_numbers |= {a, b}

print sum(amicable_numbers)
