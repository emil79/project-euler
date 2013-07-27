"""
Algorithm: start on the penultimate row. For each number in this row, add the
maximum of the two beneath it. Repeat for each row, ascending until the top
is reached. Print out the very top number.
"""

with open("data/67/triangle.txt") as f:
    data = f.read()

numbers = [map(int, line.split()) for line in data.split("\n") if line]

for i in reversed(range(len(numbers) - 1)):
    for j in range(i + 1):
        numbers[i][j] += max(numbers[i + 1][j: j + 2])

print numbers[0][0]
