def ways_to_make(n, coin_values):
    if n == 0:
        return 1
    if not coin_values:
        return 0
    value, remaining = coin_values[0], coin_values[1:]
    return sum(ways_to_make(n - m, remaining) for m in range(0, n + 1, value))

print ways_to_make(200, (1, 2, 5, 10, 20, 50, 100, 200))
