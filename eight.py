""" AoC 2017 Day 8 """


import csv
with open('eight.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    lines = list(reader)
    var = []
    val = []
    max_val = 0
    for line in lines:
        var1 = line[0]
        inst1 = line[1]
        val1 = int(line[2])
        var2 = line[4]
        inst2 = line[5]
        val2 = int(line[6])
        if var1 in var:
            var1_val = val[var.index(var1)]
        else:
            var.append(var1)
            val.append(0)
            var1_val = 0
        if var2 in var:
            var2_val = val[var.index(var2)]
        else:
            var.append(var2)
            val.append(0)
            var2_val = 0
        if inst2 == '>=':
            if var2_val >= val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        if inst2 == '<=':
            if var2_val <= val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        if inst2 == '==':
            if var2_val == val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        if inst2 == '<':
            if var2_val < val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        if inst2 == '>':
            if var2_val > val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        if inst2 == '!=':
            if var2_val != val2:
                if inst1 == 'dec':
                    var1_val -= val1
                else:
                    var1_val += val1
        val[var.index(var1)] = var1_val
        if var1_val > max_val:
            max_val = var1_val
    print(var)
    print(val)
    print(max(val))
    print(max_val)
