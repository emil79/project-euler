from itertools import product
import json

numbers = json.loads("[{}]".format(open("data/59/cipher1.txt").read()))

for key in product(range(ord('a'), ord('z') + 1), repeat=3):
    transformed_numbers = [n ^ key[i % 3] for i, n in enumerate(numbers)]
    plaintext = "".join(chr(n) for n in transformed_numbers)
    if "there" in plaintext:
        print sum(transformed_numbers)
        break
