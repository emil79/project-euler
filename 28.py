# By hand, we can see that the answer is the sum of one plus
# x^2 - 6(x-1) for odd x from 3 to 1001 inclusive.
print 1 + sum(4 * x ** 2 - 6 * x + 6 for x in range(3, 1002, 2))
