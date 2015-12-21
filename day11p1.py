import itertools
import re
import string

inputString = "vzbxkghb"
allowed = list("abcdefghjkmnpqrstuvwxyz")
straight = [string.ascii_lowercase[i:i+3] for i in range(0,24)]
prog = re.compile(r"(\w)\1\w*(\w)\2")


def next_string(password):
    output = []
    overflow = 0

    for p in reversed(password):
        pos = allowed.index(p) + overflow
        pos += 1 if len(output) == 0 else 0
        char = allowed[pos % len(allowed)]
        overflow = 1 if pos >= len(allowed) else 0
        output.append(char)

    return ''.join(reversed(output))


def next_password(password):
    while True:
        password = next_string(password)
        if prog.search(password) and len(set(prog.search(password).groups())) == 2:
            for s in straight:
                if s in password:
                    return password


inputString = next_password(inputString)
print(inputString)
