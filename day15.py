#!/usr/bin/env python3
import re

def get_input():
    with open('day15.txt') as f:
        discs = {}
        for line in f:
            m = re.match('Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).',line)
            if m:
                discs[int(m.group(1))] = {'positions':int(m.group(2)),'start':int(m.group(4)),'position':int(m.group(4))}
            else:
                print('Input error')
    return discs

def part1(discs):
    for t in range(100000000):
        currents = []
        for disc in range(1,len(discs)+1):
            position = discs[disc]['start']+t+disc
            discs[disc]['position'] = position % discs[disc]['positions']
            currents.append(str(position % discs[disc]['positions']))
        #print(t,currents)
        if currents == ['0']*len(currents):
            return t

print(part1(get_input()))
