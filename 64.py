from math import sqrt

# For algorithm see
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion


def sqrt_continued_fraction(N):
    a0 = int(sqrt(N))
    m, d, a = 0, 1, a0
    triplets = []
    digits = []
    while not (m, d, a) in triplets:
        triplets.append((m, d, a))
        digits.append(a)
        m = d * a - m
        d = (N - m ** 2) / d
        if d == 0:
            return digits, 0
        a = int((a0 + m) / d)
    period = len(triplets) - triplets.index((m, d, a))
    return digits, period


count = 0
for n in range(10001):
    digits, period = sqrt_continued_fraction(n)
    if period % 2:
        count += 1
print count
