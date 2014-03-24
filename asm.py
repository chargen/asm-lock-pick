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
}

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

def execute_command(cmd):
    if cmd[0] == 'mov':
        assert is_reg(cmd[1])
        assert is_reg(cmd[2]) or is_num(cmd[2])
        regs[cmd[1]] = get_value(cmd[2])
    elif cmd[0] == 'add':
        assert is_reg(cmd[1])
        assert is_reg(cmd[2]) or is_num(cmd[2])
        regs[cmd[1]] += get_value(cmd[2])
    elif cmd[0] == 'sub':
        assert is_reg(cmd[1])
        assert is_reg(cmd[2]) or is_num(cmd[2])
        regs[cmd[1]] -= get_value(cmd[2])
    elif cmd[0] == 'mul':
        assert is_reg(cmd[1])
        assert is_reg(cmd[2]) or is_num(cmd[2])
        regs[cmd[1]] *= get_value(cmd[2])
    elif cmd[0] == 'div':
        assert is_reg(cmd[1])
        assert is_reg(cmd[2]) or is_num(cmd[2])
        regs[cmd[1]] /= get_value(cmd[2])
    elif cmd[0] == 'ret':
        print regs['rv']

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
