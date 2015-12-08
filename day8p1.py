import re
from ast import literal_eval

inputString = [line.rstrip('\n') for line in open('day8.txt')]
r = []
c = []

for s in inputString:
    dehexify = re.sub(r"(\\x[0-f]{2})", "a", s)
    clean = literal_eval(dehexify);
    r.append(len(s))
    c.append(len(clean))

print(sum(r) - sum(c))