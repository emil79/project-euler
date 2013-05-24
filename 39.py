counts = dict((i, 0) for i in range(1001))
squares = [i ** 2 for i in range(1001)]

# We may assume that the i is the length of the
# shortest side and j is the length of the next
# shortest side.
for i in range(1, 333):
    for j in range(i, 666):
        s = i ** 2 + j ** 2
        if s in squares:
            k = squares.index(s)
            p = i + j + k
            if p < 1000:
                counts[p] += 1

print sorted(counts, key=lambda i: counts[i])[-1]
