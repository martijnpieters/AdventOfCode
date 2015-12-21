lines = [line.rstrip('\n') for line in open('day16.txt')]
sues = {}
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
    sue = int(sue[:-1])
    property1 = property1[:-1]
    property2 = property2[:-1]
    property3 = property3[:-1]
    sues[sue] = {
        'children': None,
        'cats': None,
        'samoyeds': None,
        'pomeranians': None,
        'akitas': None,
        'vizslas': None,
        'goldfish': None,
        'trees': None,
        'cars': None,
        'perfumes': None
    }
    sues[sue][property1] = int(value1[:-1])
    sues[sue][property2] = int(value2[:-1])
    sues[sue][property3] = int(value3)

    if tape[property1] == sues[sue][property1] and tape[property2] == sues[sue][property2] and tape[property3] == sues[sue][property3]:
        print(sue)
        exit()
