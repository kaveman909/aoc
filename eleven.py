""" AoC 2017 Day 11 """


import csv
from math import sin, cos, tan, pi, sqrt

with open('eleven.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    pin = list(reader)[0]
th = pi / 6
N = [0, 1]
S = [0, -1]
NE = [cos(th), sin(th)]
SE = [cos(th), -sin(th)]
NW = [-cos(th), sin(th)]
SW = [-cos(th), -sin(th)]

pin = [N if i == 'n' else i for i in pin]
pin = [S if i == 's' else i for i in pin]
pin = [NE if i == 'ne' else i for i in pin]
pin = [SE if i == 'se' else i for i in pin]
pin = [NW if i == 'nw' else i for i in pin]
pin = [SW if i == 'sw' else i for i in pin]

sums = [0, 0]
max_steps = 0
count = 0
for i, j in pin:
    count += 1
    sums[0] += i
    sums[1] += j
    suma = [abs(x) for x in sums]
    if (suma[1] / suma[0] > tan(th)):
        h = abs(suma[0] / cos(th))
        y = abs(h * sin(th))
        d = round(h + suma[1] - y)
    else:
        d = round(suma[0] / cos(th))
    if (d > max_steps):
        max_steps = d
    if count == len(pin):
        print('Part 1: {}'.format(d))
print('Part 2: {}'.format(max_steps))
