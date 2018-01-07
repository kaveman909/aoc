import re
# Parse input
with open('twenty.txt') as f:
    lines = f.readlines()
mlist = []
for line in lines:
    lst = []
    openc = [m.start() for m in re.finditer('<', line)]
    closec = [m.start() for m in re.finditer('>', line)]
    for i in range(len(openc)):
        lst.append([int(j) for j in (line[openc[i] + 1:closec[i]]).split(',')])
    mlist.append(lst)

# Find minimum acceleration
min_val = 100000
ind = 0
for line in mlist:
    a = line[2]
    a_man = sum([abs(i) for i in a])
    if a_man < min_val:
        min_val = a_man
        min_ind = ind
    ind += 1
print('Part 1: {}'.format(min_ind))

# nlist = []
# for line in mlist:
    # check for duplicates
        
