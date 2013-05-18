palindromes = set()
for i in range(100, 1000):
    for j in range(i, 1000):
        s = str(i * j)
        if s[::-1] == s:
            palindromes.add(i * j)
print sorted(palindromes)[-1]
