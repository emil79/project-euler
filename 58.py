from math import sqrt


def is_prime(n):
    return not any(n % i == 0 for i in range(2, int(sqrt(n) + 1)))

prime_count, total = 8, 13
i = 7
while prime_count * 1.0 / total >= 0.1:
    i += 2
    prime_count += sum(1 for j in range(1, 4)
                       if is_prime(i ** 2 - (i - 1) * j))
    total += 4
print i
