""" AoC 2017 Day 17 """


LAST = 2017
TIMES = 50000000
dist = 371
lst = [0]
cur_p = 0
ins_n = 1
while ins_n < (LAST + 1):
    new_p = ((dist + cur_p) % ins_n) + 1
    lst.insert(new_p, ins_n)
    cur_p = new_p
    ins_n += 1
print('Part 1: {}'.format(lst[lst.index(LAST) + 1]))

lst = [0] * TIMES
cur_p = 0
ins_n = 1
while ins_n < (TIMES + 1):
    new_p = ((dist + cur_p) % ins_n) + 1
    lst[new_p] = ins_n
    cur_p = new_p
    ins_n += 1
print('Part 2: {}'.format(lst[lst.index(0) + 1]))
