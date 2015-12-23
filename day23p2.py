import re

lines = [line.rstrip('\n') for line in open('day23.txt')]
instructions = []
registers = {
    'a': 1,
    'b': 0
}
regex = re.compile(r'([a-z]+) ([\w\+\-]+)(?:\, ([\w\+\-]+))?')


def run_instruction(number):
    next_instruction = None
    instruction = instructions[number]
    command = instruction[0]

    if command == 'hlf':  # Half
        registers[instruction[1]] = int(registers[instruction[1]] / 2)
    elif command == 'tpl':  # Triple
        registers[instruction[1]] = int(registers[instruction[1]] * 3)
    elif command == 'inc':  # Increase with 1
        registers[instruction[1]] += 1
    elif command == 'jmp':  # Jump relative
        next_instruction = number + int(instruction[1])
    elif command == 'jie':  # Jump if even
        if registers[instruction[1]] % 2 == 0:
            next_instruction = number + int(instruction[2])
    elif command == 'jio':  # Jump if one
        if registers[instruction[1]] == 1:
            next_instruction = number + int(instruction[2])
    else:
        print('Unrecognized instruction: ' + command)

    if next_instruction == None:
        next_instruction = number + 1

    return next_instruction

for line in lines:
    instruction = list(regex.search(line).groups())
    if instruction[2]:
        instruction[2] = int(instruction[2])
    instructions.append(instruction)

next_instruction = 0
while True:
    next_instruction = run_instruction(next_instruction)
    if next_instruction >= len(instructions):
        print(registers)
        exit()
