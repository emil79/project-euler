from itertools import permutations

# We can see that the products have to be of the form
# XX * YYY = ZZZZ or X * YYYY = ZZZZ
# So we generate all the possible digit combinations and
# see which ones work.

products = set()
for p in permutations("123456789"):
    s = "".join(p)
    a, b, c = int(s[0:2]), int(s[2:5]), int(s[5:9])
    if a * b == c:
        products.add(c)
    d, e, f = int(s[0:1]), int(s[1:5]), int(s[5:9])
    if d * e == f:
        products.add(f)

print sum(products)
