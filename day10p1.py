import itertools

s = "3113322113"
for i in range(40):
    groups = [list(g) for k, g in itertools.groupby(s)]
    s = ''.join([str(len(group)) + group[0] for group in groups])

print len(s)