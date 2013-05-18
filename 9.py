# Runs fast enough, but may as well assume a is the smallest. And
# c has to be the largest of the three, so we can assume that b
# is less than 500.
for a in range(333):
    for b in range(a, 500):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print a * b * c
