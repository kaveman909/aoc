""" AoC 2017 Day 7 """


from anytree import Node, RenderTree
from anytree.exporter import DotExporter

with open('seven.txt') as f:
    lines = [i.rstrip() for i in f.readlines()]
lines = [i.split(' ') for i in lines]
lines = [[i.strip('(),') for i in line] for line in lines]
lines = [[int(i) if i.isdigit() else i for i in line] for line in lines]
# print(lines)
node_dict = {}
# setup all the nodes with weights (no children)
for line in lines:
    name = line[0]
    weight = line[1]
    node_dict[name] = Node(name, w=weight)

# assign the parent/child relationships
for line in lines:
    if len(line) > 2:
        parent = line[0]
        children = line[3:]
        for child in children:
            node_dict[child].parent = node_dict[parent]

# root can be found from any node
root = node_dict[lines[0][0]].root
print('Part 1: {}'.format(root.name))

# manually find child that is too light/heavy
# todo: improve to automate solution
for child in node_dict['apktiv'].children:
    print('child: {}'.format(child.name))
    node_sum = child.w
    #node_sum = 0
    for descendant in child.descendants:
        node_sum += descendant.w
    print('weight: {}'.format(node_sum))
