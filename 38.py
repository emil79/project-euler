def product(n, t):
    return int("".join(str(n * x) for x in t))


def is_pandigital(n):
    s = str(n)
    return len(s) == 9 and \
        all(str(i) in s for i in range(1, 10))


pandigital_numbers = set()
for i in range(2, 10):
    for k in range(1, 10 ** (9 / i)):
        n = product(k, range(1, i + 1))
        if is_pandigital(n):
            pandigital_numbers.add(n)
print max(pandigital_numbers)
