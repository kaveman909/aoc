""" AoC 2017 Day 12 """


import re


def get_connections(node, connections, mapping):
    """ appends unique nodes to the connections from the mapping """
    for i in mapping[node]:
        if int(i) not in connections:
            connections.append(int(i))


# read in lines from file
with open('twelve.txt', 'r') as f:
    lines = f.readlines()
# parse lines for numerical content
pin = []
for line in lines:
    lst = re.findall(r'\d+', line)
    pin.append(lst)
connections = []
groups = []

for j in range(2000):
    get_connections(j, connections, pin)
    for i in connections:
        get_connections(i, connections, pin)
    connections.sort()
    if j == 0:
        print('Part 1: {}'.format(len(connections)))
    if connections not in groups:
        groups.append(connections)
    connections = []

print('Part 2: {}'.format(len(groups)))
