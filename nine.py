with open('nine.txt', 'r') as f:
    p1 = f.readline()
p2 = []
# (1) clean up and count garbage
garbage = False
ignore_next = False
garbage_count = 0
for i in p1:
    if ignore_next == True:
        ignore_next = False
    elif (garbage == False) and (i == '<'):
        garbage = True
    elif (garbage == True) and (i == '!'):
        ignore_next = True
    elif garbage == False:
        p2.append(i)
    elif (garbage == True) and (i == '>'):
        garbage = False
    elif (garbage == True):
        garbage_count += 1
print('garbage count = {}'.format(garbage_count))

# (2) count the levels / points
level = 0
total = 0
for i in p2:
    if i == '{':
        level += 1
        total += level
    elif i == '}':
        level -= 1
print('total points = {}'.format(total))
