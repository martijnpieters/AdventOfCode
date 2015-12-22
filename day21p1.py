import sys
import itertools

weapons = [
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]
armor = [
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5],
    [0, 0, 0]
]
rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]
boss_hit = 104
boss_damage = 8
boss_armor = 1
own_hit = 100
min_costs = sys.maxint


def get_game_costs(w, a, *args):
    costs = w[0] + a[0]
    damage = w[1] + a[1]
    armor = w[2] + a[2]
    for r in args:
        costs += r[0]
        damage += r[1]
        armor += r[2]

    o_hit = own_hit
    b_hit = boss_hit
    i = 0

    while o_hit > 0 and b_hit > 0:
        if i % 2 == 0: # My turn
            b_hit -= (damage - boss_armor) if (damage - boss_armor) >= 1 else 1
        else: # Boss turn
            o_hit -= (boss_damage - armor) if (boss_damage - armor) >= 1 else 1
        i += 1

    return costs if o_hit > 0 else sys.maxint

for w in weapons:
    for a in armor:
        # Zero rings
        c = get_game_costs(w, a)
        if c < min_costs:
            min_costs = c

        # One ring
        for r in rings:
            c = get_game_costs(w, a, r)
            if c < min_costs:
                min_costs = c

        # Two rings
        for r1, r2 in itertools.combinations(rings, 2):
            c = get_game_costs(w, a, r1, r2)
            if c < min_costs:
                min_costs = c

print(min_costs)
