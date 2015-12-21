lines = [line.rstrip('\n') for line in open('day14.txt')]
reindeers = {}


def get_distance(reindeer, time):
    distance = 0
    while True:
        d = reindeer['d'] if time - reindeer['d'] > 0 else time
        distance += reindeer['s'] * d
        time -= d
        time -= reindeer['r']
        if time <= 0:
            return distance

for line in lines:
    name, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = line.split(' ')
    speed = int(speed)
    duration = int(duration)
    rest = int(rest)
    reindeers[name] = get_distance({'s': speed, 'd': duration, 'r': rest}, 2503)

print(reindeers)
