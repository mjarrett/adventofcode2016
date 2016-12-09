#!/usr/bin/env python3
import re



with open('day9.txt') as f:
    line = f.read()
    go = True
    ignore = (0,0)
    print(line)
    while go:
        m = re.search('\((\d+)x(\d+)\)',line)
        if m:
            print('({}x{})'.format(m.group(1),m.group(2)))
            if m.start() not in range(ignore[0],ignore[1]):

                t = [m.start(),m.end(),int(m.group(1)),int(m.group(2))]
                line = line[0:t[0]] + line[t[1]:t[1]+t[2]]*t[3] + line[t[1]+t[2]:]
                ignore = (t[0],t[0]+t[2]*t[3])
            # Need to split up line so only the new stuff gets fed into regex

        else:
            go = False
    print(len(line))
    print('****')
