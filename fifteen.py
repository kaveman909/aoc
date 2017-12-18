""" AoC 2017 Day 15 """


a_hist = 591
b_hist = 393

a_factor = 16807
b_factor = 48271
divisor = 2147483647

judge_count = 0
for _ in range(40000000):
    a_cur = a_hist * a_factor
    b_cur = b_hist * b_factor

    a_cur %= divisor
    b_cur %= divisor

    if (a_cur & 0xFFFF) == (b_cur & 0xFFFF):
        judge_count += 1
    a_hist = a_cur
    b_hist = b_cur
print('Part 1: {}'.format(judge_count))

a_list = []
b_list = []
judge_count = 0
pairs = 0
while pairs < 5000000:
    a_cur = a_hist * a_factor
    b_cur = b_hist * b_factor

    a_cur %= divisor
    b_cur %= divisor

    if (a_cur % 4) == 0:
        a_list.append(a_cur)
    if (b_cur % 8) == 0:
        b_list.append(b_cur)

    a_hist = a_cur
    b_hist = b_cur

    pairs = min([len(a_list), len(b_list)])
for i in range(5000000):
    if (a_list[i] & 0xFFFF) == (b_list[i] & 0xFFFF):
        judge_count += 1
print('Part 2: {}'.format(judge_count))
