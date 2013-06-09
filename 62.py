digits_to_cubes = {}
for n in range(1, 10000):
    ordered_digits = tuple(sorted(str(n ** 3)))
    digits_to_cubes.setdefault(ordered_digits, []).append(n)

candidates = set()
for digits, cubes in digits_to_cubes.items():
    if len(cubes) == 5:
        candidates.add(min(cubes) ** 3)
print min(candidates)
