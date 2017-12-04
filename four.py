""" AoC 2017 Day 4 """


import csv

with open('four.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    lines = list(reader)
    for part in [1, 2]:
        good = 0
        for line in lines:
            bad = 0
            for i in range(len(line)):
                for j in range(i + 1, len(line)):
                    if part == 1:
                        if line[i] == line[j]:
                            bad = 1
                            break
                    if part == 2:
                        if ''.join(sorted(line[i])) == ''.join(sorted(line[j])):
                            bad = 1
                            break
            if bad == 0:
                good += 1
        print(good)
