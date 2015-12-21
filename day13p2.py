import itertools

lines = [line.rstrip('\n') for line in open('day13.txt')]
happiness = {}
names = ['Martijn']
best_score = 0
best_permutation = None


for line in lines:
    name1, _, gain, amount, _, _, _, _, _, _, name2 = line.split(' ')
    name2 = name2[:-1]
    amount = int(amount) if gain == 'gain' else -int(amount)

    happiness[(name1, name2)] = amount
    if name1 not in names:
        names.append(name1)
        happiness[('Martijn', name1)] = 0
        happiness[(name1, 'Martijn')] = 0

for c in itertools.permutations(names):
    l = list(c)
    score = 0

    for i in range(len(l)):
        name1 = l[i]
        name2 = l[(i+1) % len(l)]
        score += happiness[(name1, name2)] + happiness[(name2, name1)]

    if score > best_score:
        best_score = score
        best_permutation = c

print(best_score)
print(best_permutation)
