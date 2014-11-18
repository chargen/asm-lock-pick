#!/usr/bin/env python

import sys

from executor import (
     Bit8Executor, Bit16Executor
)

def main():
    if len(sys.argv) != 3:
        print('Usage: %s <file> <stack>' % (sys.argv[0],))
        return
    with open(sys.argv[1], 'r+') as file:
        cmds = []
        for line in file:
            line = line.strip()
            if line == '' or line[0] == '#':
                continue
            cmd = line.split()
            cmds.append(cmd)

        stack = sys.argv[2]
        executor_8 = Bit8Executor(stack)
        executor_8.execute(cmds)

        executor_16 = Bit16Executor(stack)
        executor_16.execute(cmds)

if __name__ == '__main__':
    main()
