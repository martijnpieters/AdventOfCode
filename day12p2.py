import json

numbers = []


def get_numbers(data):
    skip = False

    for i in data:
        d = data.get(i) if isinstance(data, dict) else None
        if d == "red":
            skip = True
            break

    if not skip:
        for i in data:
            d = data.get(i) if isinstance(data, dict) else i
            if isinstance(d, dict) or isinstance(d, list):
                get_numbers(d)
            elif isinstance(d, int):
                numbers.append(d)

with open('day12.txt') as raw:
    data = json.load(raw)
    get_numbers(data)
    print(sum(numbers))
