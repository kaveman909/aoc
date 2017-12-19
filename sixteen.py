with open('sixteen.txt') as f:
    line = f.readline()
pin = line.split(',')

SPIN = 's'
EXCH = 'x'
PART = 'p'

dancers_in = 'abcdefghijklmnop'
#dancers = 'abcde'
dancers = [i for i in dancers_in]

for j in range(40):
    for i in pin:
        inst = i[0]
        data = i[1:].split('/')
        data = [int(j) if j.isdigit() else j for j in data]

        if inst == SPIN:
            dancers = dancers[-data[0]:] + dancers[0:len(dancers) - data[0]]
        elif inst == EXCH:
            temp = dancers[data[0]]
            dancers[data[0]] = dancers[data[1]]
            dancers[data[1]] = temp
        elif inst == PART:
            indx0 = dancers.index(data[0])
            indx1 = dancers.index(data[1])
            dancers[indx0] = data[1]
            dancers[indx1] = data[0]
    if j == 0:
        print('Part 1: {}'.format(''.join(dancers)))
    if ''.join(dancers) == dancers_in:
        print(j, dancers_in)
print('Part 2: {}'.format(''.join(dancers)))
