import re

lines = [line.rstrip('\n') for line in open('day19.txt')]
empty = False
molecule = None
molecules = []
replacements = []

for line in lines:
    if not empty:
        if len(line) == 0:
            empty = True
        else:
            pattern, replacement = line.split(' => ')
            replacements.append([pattern, replacement])
    else:
        molecule = line

for r in replacements:
    pattern = r[0]
    replacement = r[1]
    for pos in [m.start() for m in re.finditer(pattern, molecule)]:
        new_molecule = molecule[:pos] + replacement + molecule[pos + len(pattern):]
        if new_molecule not in molecules:
            molecules.append(new_molecule)

print(len(molecules))
