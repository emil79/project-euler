from itertools import permutations

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

rows = (
    (0, 1, 2),
    (3, 2, 4),
    (5, 4, 6),
    (7, 6, 8),
    (9, 8, 1),
)

solutions = []

for P in permutations(numbers):
    if all(P[row[0]] >= P[rows[0][0]] for row in rows):
        if len({sum(P[i] for i in row) for row in rows}) == 1:
            solutions.append(''.join(str(P[i]) for row in rows for i in row))

print max(solutions)
