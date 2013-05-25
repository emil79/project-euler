# I feel I've cheated at this; we get the right answer but
# the program doesn't prove that the difference found is the
# smallest such one. I might revisit this problem.

pentagonals = [n * (3 * n - 1) / 2 for n in range(1, 3000)]
pentagonals_set = set(pentagonals)

differences = set()
for k in range(len(pentagonals) - 1):
    for j in range(k, len(pentagonals)):
        if pentagonals[j] + pentagonals[k] in pentagonals_set:
            difference = pentagonals[j] - pentagonals[k]
            if difference in pentagonals_set:
                differences.add(difference)
print min(differences)
