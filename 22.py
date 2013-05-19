import json

with open("data/22/names.txt") as f:
    names = json.loads('[' + f.read() + ']')

total = 0
for i, name in enumerate(sorted(names)):
    total += (i + 1) * sum(ord(c) - ord('A') + 1 for c in name)
print total
