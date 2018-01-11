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
#print(mlist, len(mlist))
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

for k in range(50):
    # check for duplicates
    for i in range(len(mlist)):
        dup = False
        dup_list = []
        for j in range(len(mlist)):
            try:
                if (mlist[i][0] == mlist[j][0]) and (i != j):
                    dup = True
                    dup_list.append(mlist[j])
            except:
                pass
        if dup:
            dup_list.append(mlist[i])
            mlist = [l for l in mlist if l not in dup_list]

    # update position and velocity
    for vector in mlist:
        p = vector[0]
        v = vector[1]
        a = vector[2]
        v = [i + j for i, j in zip(v, a)]
        p = [i + j for i, j in zip(p, v)]
        vector[0] = p
        vector[1] = v
print('Part 2: {}'.format(len(mlist)))
