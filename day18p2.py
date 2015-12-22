import numpy as np

lines = [line.rstrip('\n') for line in open('day18.txt')]
size = len(lines)
current_state = np.zeros((size, size), dtype=np.bool)
next_state = np.zeros((size, size), dtype=np.bool)

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if (x == 0 and y == 0) or (x == 0 and y == size - 1) or (x == size - 1 and y == 0) or (x == size - 1 and y == size - 1):
            current_state[x][y] = True
        else:
            current_state[x][y] = True if c == '#' else False

for n in xrange(100):
    for (x, y), value in np.ndenumerate(current_state):
        minx = x - 1 if x > 0 else x
        maxx = x + 2 if x < size - 1 else x + 1
        miny = y - 1 if y > 0 else y
        maxy = y + 2 if y < size - 1 else y + 1

        neigbors = 0
        for i in range(minx, maxx):
            for j in range(miny, maxy):
                if not (i == x and j == y):
                    neigbors += 1 if current_state[i][j] else 0

        if (x == 0 and y == 0) or (x == 0 and y == size - 1) or (x == size - 1 and y == 0) or (x == size - 1 and y == size - 1):
            next_state[x][y] = True
        elif value:
            next_state[x][y] = True if neigbors == 2 or neigbors == 3 else False
        else:
            next_state[x][y] = True if neigbors == 3 else False

    current_state = np.copy(next_state)

print(sum(sum(current_state)))
