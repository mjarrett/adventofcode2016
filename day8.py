#!/usr/bin/env python3

import numpy as np
import re

def rect(screen,x,y):
    screen[0:x,0:y] = 1
    return screen

def rot_row(screen,i,x):
    screen[i] = np.roll(screen[i],x)
    return screen

def rot_col(screen,i,y):
    screen[:,i] = np.roll(screen[:,i],y)
    return screen



def part1():
    screen = np.zeros((6,50))
    with open('day8.txt') as f:
        for line in f:
            m = re.search('rect (\d+)x(\d+)',line)
            n = re.search('rotate row y=(\d+) by (\d+)',line)
            p = re.search('rotate column x=(\d+) by (\d+)',line)
            if m:
                screen = rect(screen,int(m.group(2)),int(m.group(1)))
            elif n:
                screen = rot_row(screen,int(n.group(1)),int(n.group(2)))
            elif p:
                screen = rot_col(screen,int(p.group(1)),int(p.group(2)))
            else:
                print('input error')
                print(line)
            #print(screen)
            #print('****')

    print(np.sum(screen))

    for i in range(0,50,5):
        print(screen[:,i:i+5])
        print("******")
part1()
