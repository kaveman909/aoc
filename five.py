g_lines = []
with open('five.txt', 'r') as f:
    for line in f:
        g_lines.append(int(line))

lines = list(g_lines)
i = 0
count = 0
while i < len(lines):
    i_old = i
    i += lines[i]
    lines[i_old] += 1
    count += 1
print('Part 1: {}'.format(count))

lines = list(g_lines)
i = 0
count = 0
while i < len(lines):
    i_old = i
    i += lines[i]
    if lines[i_old] >= 3:
        lines[i_old] -= 1
    else:
        lines[i_old] += 1
    count += 1
print('Part 2: {}'.format(count))
