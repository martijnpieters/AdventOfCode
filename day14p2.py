lines = [line.rstrip('\n') for line in open('day14.txt')]
reindeers = {}
scores = {}
time = 2503


def get_distance(reindeer, time):
    distance = []

    for s in range(time):
        is_moving = (s % (reindeer['d'] + reindeer['r']) < reindeer['d'])

        if is_moving and len(distance) > 0:
            distance.append(reindeer['s'] + distance[-1])
        elif is_moving:
            distance.append(reindeer['s'])
        else:
            distance.append(distance[-1])

    return distance

for line in lines:
    name, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = line.split(' ')
    speed = int(speed)
    duration = int(duration)
    rest = int(rest)
    reindeers[name] = get_distance({'s': speed, 'd': duration, 'r': rest}, time)
    scores[name] = 0

for s in range(time):
    best_reindeers = []
    best_score = 0

    for name in reindeers.keys():
        reindeer = reindeers[name]

        if reindeer[s] > best_score:
            best_score = reindeer[s]
            best_reindeers = [name]
        elif reindeer[s] == best_score:
            best_reindeers.append(name)

    for name in best_reindeers:
        scores[name] += 1

print(scores)
