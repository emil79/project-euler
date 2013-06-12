def e():
    yield 2
    yield 1
    k = 2
    while True:
        yield k
        yield 1
        yield 1
        k += 2

# Using well-known recurrence relation; see e.g.
# http://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems

H = [0, 1]
for a in e():
    H.append(a * H[-1] + H[-2])
    if len(H) == 102:
        break

print sum(int(d) for d in str(H[-1]))
