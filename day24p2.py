import itertools
import sys

packages = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
total = sum(packages)
onefourth = total / 4
best_QE = sys.maxint
best_amount = sys.maxint

print(total)
print(onefourth)

for i1 in xrange(2, len(packages) - 5):
    for c1 in itertools.combinations(packages, i1):
        if sum(c1) == onefourth:
            fours_possible = False
            packages_left = packages[:]
            for p in c1:
                packages_left.remove(p)
                
            for i2 in xrange(2, len(packages_left) - 3):
                for c2 in itertools.combinations(packages_left, i2):
                    if sum(c2) == onefourth:
                        
                        packages_left2 = packages[:]
                        for p in c2:
                            packages_left2.remove(p)
                        
                        for i3 in xrange(2, len(packages_left) - 2):
                            for c3 in itertools.combinations(packages_left2, i3):
                                if sum(c2) == onefourth:
                                    fours_possible = True
                                    break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                        
                else:
                    continue
                break
            else:
                continue
            
            if fours_possible:
                c1 = sorted(c1)
                QE = reduce(lambda x, y: x * y, c1)
                if len(c1) <= best_amount and QE < best_QE:
                    best_amount = len(c1)
                    best_QE = QE
                elif len(c1) > best_amount:
                    print(best_QE)
                    exit()
