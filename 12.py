from math import sqrt


def number_of_divisors(n):
    d = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            d += 1 if i * i == n else 2
    return d


t, i = 1, 2
while number_of_divisors(t) <= 500:
    t, i = t + i, i + 1

print t
