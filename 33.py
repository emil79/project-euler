from fractions import Fraction

product = Fraction(1)
for i in range(10, 99):
    for j in range(i + 1, 100):
        if i % 11 and j % 11:      # Exclude things like 33/99
            a, b = str(i), str(j)
            if a[1] == b[0] and int(a[0]) * j == int(b[1]) * i:
                product *= Fraction(i, j)

print product.denominator
