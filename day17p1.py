import itertools

lines = [line.rstrip('\n') for line in open('day17.txt')]
containers = []
number = 0

for line in lines:
    container = int(line)
    containers.append(container)

for i in range(1, len(containers) + 1):
    for c in itertools.combinations(containers, i):
        if sum(c) == 150:
            print(c)
            number += 1

print(number)
