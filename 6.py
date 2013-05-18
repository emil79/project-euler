# We need the sum of of all the terms in the expansion of
# (1 + 2 + ... + 100)^2 that are not of the form i * i.
n = 100
total = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        total += 2 * i * j
print total
