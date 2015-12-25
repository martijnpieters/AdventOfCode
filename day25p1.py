m = 252533
d = 33554393
v = 20151125

p = [3010, 3019]
row = 1
col = 1
i = 1

while True:
    if row == 1:
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1
    
    i += 1
    v = (v * m) % d
    
    if row == p[0] and col == p[1]:
        print(row,col,i,v)
        exit()
