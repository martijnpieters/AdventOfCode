from random import shuffle
import re
import sys

lines = [line.rstrip('\n') for line in open('day19.txt')]
empty = False
molecule = None
molecules = []
replacements = []


def generate_molecule():
    def next_step(mol, steps):
        if mol == 'e':
            print(steps)
            return steps
        else:
            min_steps = sys.maxint

            for r in replacements:
                pattern = r[1]
                replacement = r[0]

                for pos in [m.start() for m in re.finditer(pattern, mol)]:
                    steps += mol.count(pattern)
                    new_molecule = mol.replace(pattern, replacement)
                    current_steps = next_step(new_molecule, steps)

                    if current_steps < min_steps:
                        min_steps = current_steps

            # Insert hacky approach
            if steps > 300:
                shuffle(replacements)
                current_steps = next_step(molecule, 0)

                if current_steps < min_steps:
                    min_steps = current_steps

            return min_steps

    return next_step(molecule, 0)

for line in lines:
    if not empty:
        if len(line) == 0:
            empty = True
        else:
            pattern, replacement = line.split(' => ')
            replacements.append([pattern, replacement])
    else:
        molecule = line

replacements = sorted(replacements, key=lambda replacement: len(replacement[1]), reverse=True)
print(generate_molecule())
