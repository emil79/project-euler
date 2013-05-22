# 9^5 * 7 is only 6 digits, so we need only
# consider numbers of at most 6 digits.

numbers = []
for i in range(10, 1000000):
    if sum(int(x) ** 5 for x in str(i)) == i:
        numbers.append(i)

print sum(numbers)
