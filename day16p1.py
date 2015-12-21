lines = [line.rstrip('\n') for line in open('day16.txt')]
tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in lines:
    _, sue, property1, value1, property2, value2, property3, value3 = line.split(' ')

    property1 = property1[:-1]
    property2 = property2[:-1]
    property3 = property3[:-1]
    aunt = {
        property1: int(value1[:-1]),
        property2: int(value2[:-1]),
        property3: int(value3)
    }

    if tape[property1] == aunt[property1] and tape[property2] == aunt[property2] and tape[property3] == aunt[property3]:
        print(sue[:-1])
        exit()
