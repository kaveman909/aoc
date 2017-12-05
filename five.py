import time
g_lines = []
with open('five1.txt', 'r') as f:
    for line in f:
        g_lines.append(int(line))
start_time = time.time()
lines = list(g_lines)
i = 0
count = 0
while i < len(lines):
    i_old = i
    i += lines[i]
    lines[i_old] += 1
    count += 1
end_time = time.time()
print('Part 1: {}, {}'.format(count, end_time - start_time))

start_time = time.time()
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
end_time = time.time()
print('Part 2: {}, {}'.format(count, end_time - start_time))
