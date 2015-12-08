import re

inputString = [line.rstrip('\n') for line in open('day8.txt')]
r = []
e = []

for s in inputString:
    escaped = "\"" + re.escape(s) + "\""
    r.append(len(s))
    e.append(len(escaped))

print(sum(e) - sum(r))