#!/usr/bin/python

import sys

regs = {
  'a' : 0,
  'b' : 0,
  'c' : 0,
  'x' : 0,
  'y' : 0,
  'z' : 0,
  'i' : 0,
  'j' : 0,
  'rv' : 0,
  'sp' : 0,
}

stack = []

def is_num(arg):
    try:
        arg = int(arg)
        return 0 <= arg <= 255
    except ValueError:
        return False

def is_reg(arg):
    return arg in regs.keys()

assert is_num(10)
assert not(is_num(256))
assert not(is_num(-1))
assert is_reg('rv')

def get_value(arg):
    if is_num(arg):
        return int(arg)
    elif is_reg(arg):
        return regs[arg]
    assert False

def execute_mov(cmd):
    regs[cmd[1]] = get_value(cmd[2])

def execute_add(cmd):
    regs[cmd[1]] += get_value(cmd[2])

def execute_sub(cmd):
    regs[cmd[1]] -= get_value(cmd[2])

def execute_mul(cmd):
    regs[cmd[1]] *= get_value(cmd[2])

def execute_div(cmd):
    regs[cmd[1]] /= get_value(cmd[2])

def execute_ret(cmd):
    print regs['rv']

def execute_push(cmd):
    stack.append(get_value(cmd[1]))
    regs['sp'] += 1

def execute_pop(cmd):
    regs[cmd[1]] = stack.pop()
    regs['sp'] -= 1

execute_next = True

def execute_ife(cmd):
    global execute_next
    if not(get_value(cmd[1]) == get_value(cmd[2])):
        execute_next = False

def execute_ifn(cmd):
    global execute_next
    if not(get_value(cmd[1]) != get_value(cmd[2])):
        execute_next = False

def execute_ifg(cmd):
    global execute_next
    if not(get_value(cmd[1]) > get_value(cmd[2])):
        execute_next = False

def execute_ifl(cmd):
    global execute_next
    if not(get_value(cmd[1]) < get_value(cmd[2])):
        execute_next = False

def execute_ifge(cmd):
    global execute_next
    if not(get_value(cmd[1]) >= get_value(cmd[2])):
        execute_next = False

def execute_ifle(cmd):
    global execute_next
    if not(get_value(cmd[1]) <= get_value(cmd[2])):
        execute_next = False

protos = [
    ['mov',  ['reg', 'reg|num'],     execute_mov],
    ['add',  ['reg', 'reg|num'],     execute_add],
    ['sub',  ['reg', 'reg|num'],     execute_sub],
    ['mul',  ['reg', 'reg|num'],     execute_mul],
    ['div',  ['reg', 'reg|num'],     execute_div],
    ['ret',  [],                     execute_ret],
    ['push', ['reg|num'],            execute_push],
    ['pop',  ['reg'],                execute_pop],
    ['ife',  ['reg|num', 'reg|num'], execute_ife],
    ['ifn',  ['reg|num', 'reg|num'], execute_ifn],
    ['ifg',  ['reg|num', 'reg|num'], execute_ifg],
    ['ifl',  ['reg|num', 'reg|num'], execute_ifl],
    ['ifge', ['reg|num', 'reg|num'], execute_ifge],
    ['ifle', ['reg|num', 'reg|num'], execute_ifle],
]

def validate(proto, cmd):
    if proto[0] != cmd[0]:
        return False
    if len(proto[1]) + 1 != len(cmd):
        return False
    for i, arg in enumerate(proto[1]):
        if arg == 'reg' and not(is_reg(cmd[i + 1])):
            return False
        if arg == 'num' and not(is_num(cmd[i + 1])):
            return False
        if arg == 'reg|num' or arg == 'num|reg':
              if not(is_reg(cmd[i + 1])) and not(is_num(cmd[i + 1])):
                  return False
    return True 

def execute_command(cmd):
    global execute_next
    if not(execute_next):
        execute_next = True
        return
    for proto in protos:
        if validate(proto, cmd):
            proto[2](cmd)
            return
    assert False

def execute(cmds):
    for cmd in cmds:
        execute_command(cmd)

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <file>' % (sys.argv[0],)
        return
    with open(sys.argv[1], 'r+') as file:
        for line in file:
            cmd = line.split()
            execute_command(cmd)

if __name__ == '__main__':
    main()
