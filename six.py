""" AoC 2017 Day 6 """


import csv

with open('six.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    line = list(reader)[0]
    line = [int(a) for a in line]
    print(line)
    line_len = len(line)
    line_hist = []
    line_hist.append(list(line))
    while 1:
        # find location of max number
        max_val = max(line)
        max_index = line.index(max_val)
        #print(max_val, max_index)
        # distribute max number
        line[max_index] = 0
        while max_val > 0:
            max_index = (max_index + 1) % line_len
            line[max_index] += 1
            max_val -= 1
        # check if list matches any others
        for i in range(len(line_hist)):
            if line_hist[i] == line:
                print(line)
                print('match index = {}'.format(i))
                print('total iters = {}'.format(len(line_hist)))
                print('inf loop size = {}'.format(len(line_hist) - i))
                exit()
        # save list
        line_hist.append(list(line))
        #print(line_hist)
