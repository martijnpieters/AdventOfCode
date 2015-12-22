import numpy as np

puzzle_input = 29000000
presents = np.zeros(puzzle_input)

for i in xrange(1, puzzle_input):
    presents[i::i] += 10 * i

for i in xrange(len(presents)):
    if presents[i] >= puzzle_input:
        print(i)
        exit()
