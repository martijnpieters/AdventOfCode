import itertools
import sys

packages = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
total = sum(packages)
onethird_sum = total / 3
best_QE = sys.maxint
best_amount = sys.maxint

print(total)
print(onethird_sum)

for i1 in xrange(2, len(packages) - 3):
    for c1 in itertools.combinations(packages, i1):
        if sum(c1) == onethird_sum:
            three_thirds_possible = False
            packages_left = packages[:]
            for p in c1:
                packages_left.remove(p)
                
            for i2 in xrange(2, len(packages_left) - 1):
                for c2 in itertools.combinations(packages_left, i2):
                    if sum(c2) == onethird_sum:
                        three_thirds_possible = True
                        break
                else:
                    continue
                break
            else:
                continue
            
            if three_thirds_possible:
                c1 = sorted(c1)
                QE = reduce(lambda x, y: x * y, c1)
                if len(c1) <= best_amount and QE < best_QE:
                    best_amount = len(c1)
                    best_QE = QE
                elif len(c1) > best_amount:
                    print(best_QE)
                    exit()
