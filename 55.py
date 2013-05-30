count = 0
for n in range(1, 10000):
    s = str(n)
    for i in range(1, 50):
        s = str(int(s) + int(s[::-1]))
        if s[::-1] == s:
            break
    else:
        count += 1
print count
