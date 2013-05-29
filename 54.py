from collections import Counter

CARD_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')


def rank_hand(raw_cards):

    hand = [(CARD_VALUES.index(r[0]), r[1]) for r in raw_cards]
    values = Counter(c[0] for c in hand)
    values_value_order = sorted(values, key=lambda v: -v)
    values_count_order = sorted(values, key=lambda v: -values[v])
    signature = tuple(sorted(values.values()))
    flush = len({c[1] for c in hand}) == 1
    straight = values_value_order[0] - values_value_order[-1] == 4 \
        and len(set(values)) == 5

    if flush and straight:
        return (8, 0, values_value_order[0])
    if signature == (1, 4):
        return (7, values_count_order[0], 0)
    if signature == (2, 3):
        return (6, values_count_order[0], 0)
    if flush:
        return (5, 0, values_value_order[0])
    if straight:
        return (4, 0, values_value_order[0])
    if signature == (1, 1, 3):
        return (3, values_count_order[0], 0)
    if signature == (1, 2, 2):
        return (2, max(values_count_order[:2]), values_value_order[0])
    if signature == (1, 1, 1, 2):
        return (1, values_count_order[0], values_value_order[0])

    return (0, 0, values_value_order[0])


count = 0
with open("data/54/poker.txt") as f:
    for line in f:
        cards = line.split()
        if rank_hand(cards[:5]) > rank_hand(cards[5:]):
            count += 1
print count
