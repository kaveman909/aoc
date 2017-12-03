""" AoC Day Two """


import csv


def day_two():
    """ Day Two main function """
    with open('two.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        lines = list(reader)
        sum_list1 = []
        sum_list2 = []
        for line in lines:
            line = [int(i) for i in line]
            sum_list1.append(max(line) - min(line))
            done = 0
            for i in range(0, len(line)):
                if done == 1:
                    break
                for j in range(0, len(line)):
                    if (line[i] % line[j] == 0) and (i != j):
                        sum_list2.append(line[i] // line[j])
                        done = 1
                        break
        print(sum(sum_list1))
        print(sum(sum_list2))


day_two()
