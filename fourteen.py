""" AoC 2017 Day 14 """


from ten import knot_hash


def flood_fill(x, y, old_val, new_val):
    """ Standard recursive flood fill algorithm """
    global new_group

    if (x < 0) or (y < 0):
        return
    try:
        if hash_map[x][y] != old_val:
            return
    except IndexError:
        return
    hash_map[x][y] = new_val
    new_group = True

    flood_fill(x + 1, y, old_val, new_val)
    flood_fill(x - 1, y, old_val, new_val)
    flood_fill(x, y + 1, old_val, new_val)
    flood_fill(x, y - 1, old_val, new_val)

pin = 'hfdlxzhv'
#pin = 'flqrgnkx'
hash_sum = 0
hash_map = []
for row in range(128):
    row_s = str(row)
    hash_in = pin + '-' + row_s
    hash_out = knot_hash(hash_in)
    hash_bin = ""
    for i in hash_out:
        hash_bin += '{:08b}'.format(i)
    hash_list = [int(i) for i in hash_bin]
    hash_map.append(hash_list)
    for i in hash_bin:
        hash_sum += int(i)
print('Part 1: {}'.format(hash_sum))
cur_group = 2
x = 0
y = 0
while y < 128:
    new_group = False
    flood_fill(x, y, 1, cur_group)
    if new_group is True:
        cur_group += 1
    x += 1
    if x == 128:
        x = 0
        y += 1
for i in hash_map:
    i = [str(j) + ',' for j in i]
    i_str = ''.join(i)
    # print(i_str)
print('Part 2: {}'.format(cur_group - 2))
