from math import factorial

# 8 times 9! is only 7 digits, so we only need
# to consider numbers of at most 7 digits.

# Takes about 70 seconds; there's a lot more that
# could be done here, so I might revisit it. (I
# suspect it can be shown that curious numbers
# have to end in 5.)

factorials = [factorial(i) for i in range(10)]

curious_numbers = []
for n in range(10, 10000000):
    if sum(factorials[int(x)] for x in str(n)) == n:
        curious_numbers.append(n)
print sum(curious_numbers)
