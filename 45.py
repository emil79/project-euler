from itertools import count

triangles = (n * (n + 1) / 2 for n in count(1))
pentagonals = (n * (3 * n - 1) / 2 for n in count(1))
hexagonals = (n * (2 * n - 1) for n in count(1))

h, t, p = 0, 0, 0
while not (t == p == h and t > 40755):
    h = hexagonals.next()
    while t < h:
        t = triangles.next()
    while p < h:
        p = pentagonals.next()
print t
