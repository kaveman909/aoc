""" AoC Day One """


def sum_input(x_in):
    """ sums indexes based on the input """
    accum = 0
    for i in range(0, len(INPUT)):
        if INPUT[i] == INPUT[(i + int(x_in)) % int(len(INPUT))]:
            accum += int(INPUT[i])
    print(accum)

with open('one.txt', 'r') as f:
    INPUT = f.readline()
    sum_input(1)
    sum_input(len(INPUT) / 2)
