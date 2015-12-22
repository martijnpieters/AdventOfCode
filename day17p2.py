import itertools

lines = [line.rstrip('\n') for line in open('day17.txt')]
containers = []

for line in lines:
    container = int(line)
    containers.append(container)

for i in range(1, len(containers) + 1):
    number = 0

    for c in itertools.combinations(containers, i):
        if sum(c) == 150:
            number += 1

    if number > 0:
        print(i, number)
        exit()
