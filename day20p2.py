import numpy as np

puzzle_input = 29000000
presents = np.zeros(puzzle_input)

for i in range(1, puzzle_input):
    presents[i:51*i:i] += 11 * i

for i in range(len(presents)):
    if presents[i] >= puzzle_input:
        print(i)
        exit()
