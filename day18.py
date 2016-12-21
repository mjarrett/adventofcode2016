#!/usr/bin/env python3

with open('day18.txt') as f:
    data = list(f.read().strip())

rows = 400000
def nextline(line):
    line = ['.']+line+['.']
    nline = []
    for i in range(1,len(line)-1):
        if line[i-1] == '^' and line[i] == '^' and line[i+1] == '.':
            nline.append('^')
        elif line[i+1] == '^' and line[i] == '^' and line[i-1] == '.':
            nline.append('^')
        elif line[i+1] == '^' and line[i] == '.' and line[i-1] == '.':
            nline.append('^')
        elif line[i-1] == '^' and line[i] == '.' and line[i+1] == '.':
            nline.append('^')
        else: nline.append('.')
    return nline

line = data
floor = [line]
safe = len([x for x in floor[0] if x == '.'])
for i in range(rows-1):
    #print(safe,line)
    line = nextline(floor[i])
    floor.append(line)
    safe = safe + len( [x for x in floor[i+1] if x == '.'] )

print(len(floor))
print(safe)
