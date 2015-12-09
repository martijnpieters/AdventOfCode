import re, itertools, sys
from ast import literal_eval

lines = [line.rstrip('\n') for line in open('day9.txt')]
regex = re.compile(r"(\w+) to (\w+) = ([0-9]+)")
cities = []
dist = {}
minRoute = sys.maxint

for s in lines:
    m = regex.match(s)
    if m.group(1) not in cities:
        cities.append(m.group(1))
    if m.group(2) not in cities:
        cities.append(m.group(2))
    dist[(m.group(1), m.group(2))] = int(m.group(3))

for subset in itertools.permutations(cities, len(cities)):
    route = 0
    subset = list(subset)
    for i in range(len(subset)-1):
        a = subset[i]
        b = subset[i+1]
        if (a,b) in dist:
            route += dist[(a,b)]
        else:
            route += dist[(b,a)]
    
    if route < minRoute:
        minRoute = route

print(minRoute)