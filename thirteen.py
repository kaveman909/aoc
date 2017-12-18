""" AoC 2017 Day Thirteen """


from re import findall


def severity(time, depth, _range):
    """ finds the serverity of being caught at a given time """
    period = (2 * _range) - 2
    time = time % period
    if time <= (period / 2):
        layer = time
    else:
        layer = period - time
    if layer == 0:
        return 1, depth * _range
    else:
        return 0, 0

with open('thirteen.txt') as f:
    lines = f.readlines()
# parse lines for numerical content
pin = []
for line in lines:
    lst = findall(r'\d+', line)
    lst = [int(i) for i in lst]
    pin.append(lst)

caught_count = -1
t_start = 0
while caught_count != 0:
    caught_count = 0
    severity_sum = 0
    for depth, _range in pin:
        caught, sev = severity(depth + t_start, depth, _range)
        severity_sum += sev
        caught_count += caught
    if t_start == 0:
        print('Part 1: {}'.format(severity_sum))
    t_start += 1
print('Part 2: {}'.format(t_start - 1))
