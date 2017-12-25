from threading import Thread
from queue import Queue
from queue import Empty

with open('eighteen.txt') as f:
    lines = f.readlines()
program = [line.rstrip().split(' ') for line in lines]


def program_thread(id):
    global q
    first_time = True
    pc = 0
    snd = 0
    rcv = 0
    snd_count = 0
    registers = 'abcdefghijklmnop'
    registers = dict(zip(registers, [0] * len(registers)))
    registers['p'] = id

    while pc < len(program):
        inst = program[pc][0]
        params = [int(i) if i.lstrip('-').isdigit()
                  else i for i in program[pc][1:]]

        if inst == 'snd':
            snd = registers[params[0]]
            q[1 - id].put(snd)
            snd_count += 1
        elif inst == 'set':
            if type(params[1]) is int:
                registers[params[0]] = params[1]
            else:
                registers[params[0]] = registers[params[1]]

        elif inst == 'add':
            if type(params[1]) is int:
                registers[params[0]] += params[1]
            else:
                registers[params[0]] += registers[params[1]]
        elif inst == 'mul':
            if type(params[1]) is int:
                registers[params[0]] *= params[1]
            else:
                registers[params[0]] *= registers[params[1]]
        elif inst == 'mod':
            if type(params[1]) is int:
                registers[params[0]] %= params[1]
            else:
                registers[params[0]] %= registers[params[1]]
        elif inst == 'rcv':
            if first_time and id == 0:
                print('Part 1: {}'.format(snd))
                first_time = False
            try:
                # blocks until available for 2 seconds
                rcv = q[id].get(timeout=2)
                registers[params[0]] = rcv
            except Empty:
                if id == 1:
                    print('Part 2: {}'.format(snd_count))
                break
        elif inst == 'jgz':
            jump = False
            if type(params[0]) is int:
                if params[0] > 0:
                    jump = True
            else:
                if registers[params[0]] > 0:
                    jump = True
            if jump:
                if type(params[1]) is int:
                    pc += params[1]
                else:
                    pc += registers[params[1]]
            else:
                pc += 1
        if inst != 'jgz':
            pc += 1


q = [Queue() for _ in range(2)]

for i in range(2):
    t = Thread(target=program_thread, args=(i,))
    t.start()
