import itertools

# generate all possible states
states = list(itertools.product(
    list(range(12, 22)),
    (False, True),
    list(range(2, 12)),
))

# (dealer card, maximal player sum when should hit)
optimal_hitting_no_usable_ace = [
    (2, 12),
    (3, 12),
    (4, 11),
    (5, 11),
    (6, 11),
    (7, 16),
    (8, 16),
    (9, 16),
    (10, 16),
    (11, 16),
]
optimal_hitting_usable_ace = [
    (2, 17),
    (3, 17),
    (4, 17),
    (5, 17),
    (6, 17),
    (7, 17),
    (8, 17),
    (9, 18),
    (10, 18),
    (11, 18),
]
optimal_hit_states = set()
for hitting in optimal_hitting_no_usable_ace:
    dealer_card = hitting[0]
    for sum_player in range(12, hitting[1] + 1):
        optimal_hit_states.add((sum_player, False, dealer_card))

for hitting in optimal_hitting_usable_ace:
    dealer_card = hitting[0]
    for sum_player in range(12, hitting[1] + 1):
        optimal_hit_states.add((sum_player, True, dealer_card))
