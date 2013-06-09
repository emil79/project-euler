from itertools import count, permutations

iterators = ((n * (n + 1) / 2 for n in count(1)),
             (n ** 2 for n in count(1)),
             (n * (3 * n - 1) / 2 for n in count(1)),
             (n * (2 * n - 1) for n in count(1)),
             (n * (5 * n - 3) / 2 for n in count(1)),
             (n * (3 * n - 2) for n in count(1)))

# Build up some dictionaries, where first 2 digits map
# to possible last 2 digits
dictionaries = []
for it in iterators:
    D = {}
    for n in it:
        if n > 9999:
            break
        if n > 999:
            s = str(n)
            a, b = int(s[:2]), int(s[2:])
            D.setdefault(a, []).append(b)
    dictionaries.append(D)


# Recursive function that tries to find a path of length
# six through the list of dictionaries.
def find_paths(n, list_of_dicts):
    if not list_of_dicts:
        return [[]]
    if n in list_of_dicts[0]:
        return [[n] + R for x in list_of_dicts[0][n]
                for R in find_paths(x, list_of_dicts[1:])]
    return []

# We need to try every permutation of the dictionaries. Well,
# actually, we can assume that dictionary #5 is always the last
for P in permutations(range(5)):
    reordered_dictionaries = [dictionaries[i] for i in P + (5,)]
    for i in range(99):
        for H in find_paths(i, reordered_dictionaries):
            # We've found a path, but see if we have actually
            # found a cycle.
            if i in dictionaries[5][H[-1]]:
                print sum([int("{}{}".format(H[x - 1], H[x]))
                          for x in range(len(H))])
