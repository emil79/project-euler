def collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        yield n

# We start from 1000000 and go down. There's no point in
# considering numbers that appear in the sequences of other
# numbers, so we keep track of which ones we've seen. This
# optimization reduces the time from 38s to 19s.

seen = [False for _ in range(1000000)]
pairs = []
for i in range(999999, 0, -1):
    if not seen[i]:
        S = tuple(collatz(i))
        for j in S:
            if j < 1000000:
                seen[j] = True
        pairs.append((-len(S), i))
pairs.sort()
print pairs[0][1]
