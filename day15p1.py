lines = [line.rstrip('\n') for line in open('day15.txt')]
ingredients = {}


def find_sums(left, total, depth, numbers):
    if depth == numbers:
        return left

    dict = {}
    for i in xrange(1, left - (numbers - depth) + 1):
        dict[i] = find_sums(left - i, total, depth + 1, numbers)
    return dict


def flatten_sums(d):
    def expand(d, parent):
        if isinstance(d, dict):
            l = []
            for k, v in d.items():
                l += expand(v, parent + [k])
            return l
        else:
            return parent + [d]

    return expand(d, [])


for line in lines:
    ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split(' ')
    capacity = int(capacity[:-1])
    durability = int(durability[:-1])
    flavor = int(flavor[:-1])
    texture = int(texture[:-1])
    calories = int(calories)
    ingredients[ingredient[:-1]] = [capacity, durability, flavor, texture, calories]

ratios = find_sums(100, 100, 1, len(ingredients))
flat_ratios = flatten_sums(ratios)
best_score = 0

for i in range(len(flat_ratios) / len(ingredients)):
    n = len(ingredients)
    ratio = flat_ratios[i*n:i*n+n]
    score = 0

    for i in xrange(4):
        property_score = 0
        for j, name in enumerate(ingredients):
            ingredient_property = ingredients[name][i]
            property_score += ratio[j] * ingredient_property

        score = property_score * score if score > 0 else property_score

    if score > best_score:
        best_score = score

print(best_score)
