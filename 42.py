import json
with open("data/42/words.txt") as f:
    words = json.loads('[' + f.read() + ']')

triangle_numbers = set(i * (i + 1) / 2 for i in range(1, 1000))

count = 0
for word in words:
    n = sum(ord(c) - ord('A') + 1 for c in word)
    if n in triangle_numbers:
        count += 1
print count
