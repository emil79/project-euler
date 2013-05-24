s = ""
i = 0  # Start from 0 to make things easier
while len(s) <= 1000000:
    s += str(i)
    i += 1
print reduce(lambda x, y: x * y,
             (int(s[10 ** i]) for i in range(7)))
