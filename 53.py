from operator import mul


def binomial(n, r):
    return (reduce(mul, (n - i for i in range(r))) /
            reduce(mul, (i + 1 for i in range(r))))

print sum(1 if 2 * r == n else 2  # Only count central coefficients once
          for n in range(23, 101)
          for r in range(2, n / 2 + 1)
          if binomial(n, r) > 1000000)
