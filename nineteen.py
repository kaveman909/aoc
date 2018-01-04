""" AoC 2017 Day 19 """

with open('nineteen.txt') as f:
    lines = f.readlines()
lines = [i.rstrip('\n') for i in lines]
lines = [[i for i in line] for line in lines]

x = 99
y = 0
d = 'd'
go = True
letters = []
steps = 1

while go:
    steps += 1
    if d == 'd':
        y += 1
        if lines[y][x] != '+':
            # keep going down
            if lines[y][x] not in ['|', '-', ' ']:
                # found a letter
                letters.append(lines[y][x])
                if lines[y][x] == 'O':
                    print('Part 1: {}'.format(''.join(letters)))
                    print('Part 2: {}'.format(steps))
                    go = False
        else:
            # change direction
            if lines[y][x + 1] != ' ':
                steps += 1
                d = 'r'
                x += 1
            elif lines[y][x - 1] != ' ':
                steps += 1
                d = 'l'
                x -= 1
            else:
                go = False
    elif d == 'u':
        y -= 1
        if lines[y][x] != '+':
            # keep going up
            if lines[y][x] not in ['|', '-', ' ']:
                # found a letter
                letters.append(lines[y][x])
        else:
            # change direction
            if lines[y][x + 1] != ' ':
                steps += 1
                d = 'r'
                x += 1
            elif lines[y][x - 1] != ' ':
                steps += 1
                d = 'l'
                x -= 1
            else:
                go = False
    elif d == 'l':
        x -= 1
        if lines[y][x] != '+':
            # keep going down
            if lines[y][x] not in ['|', '-', ' ']:
                # found a letter
                letters.append(lines[y][x])
        else:
            # change direction
            if lines[y + 1][x] != ' ':
                steps += 1
                d = 'd'
                y += 1
            elif lines[y - 1][x] != ' ':
                steps += 1
                d = 'u'
                y -= 1
            else:
                go = False
    elif d == 'r':
        x += 1
        if lines[y][x] != '+':
            # keep going down
            if lines[y][x] not in ['|', '-', ' ']:
                # found a letter
                letters.append(lines[y][x])
        else:
            # change direction
            if lines[y + 1][x] != ' ':
                steps += 1
                d = 'd'
                y += 1
            elif lines[y - 1][x] != ' ':
                steps += 1
                d = 'u'
                y -= 1
            else:
                go = False
