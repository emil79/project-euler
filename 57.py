N, D = [3, 7], [2, 5]
for i in range(998):
    N.append(2 * N[-1] + N[-2])  # Calculate convergents using recurrence relation
    D.append(2 * D[-1] + D[-2])
print sum(1 for i in range(1000) if len(str(N[i])) > len(str(D[i])))
