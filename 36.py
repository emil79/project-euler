palindromes = []
for i in range(1, 1000000):
    decimal = str(i)
    binary = bin(i)[2:]
    if decimal == decimal[::-1] and binary == binary[::-1]:
        palindromes.append(i)
print sum(palindromes)
