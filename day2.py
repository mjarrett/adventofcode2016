#!/usr/bin/env python3

import numpy as np
import re



def part1():
    input = open('day2.txt')
    x = 1
    y = 1
    keys = []
    keypad = {(0,0):7,(1,0):8,(2,0):9,(0,1):4,(1,1):5,(1,2):6,(0,2):1,(1,2):2,(2,2):3}
    for line in input:
        #print(line)
        for step in line:
            #print(step)
            if step == 'U' and 0 <= y < 2:
                y = y + 1
            elif step == 'D' and 0 < y <= 2:
                y = y - 1
            elif step == 'R' and 0 <= x < 2:
                x = x + 1
            elif step == 'L' and 0 < x <= 2:
                x = x - 1
            #else:
            #    print("No move")

            #print(x,y)
        keys.append(keypad[(x,y)])
    return keys

#print(part1())

def part2():
    input = open('day2.txt')
    x = 1
    y = 1
    keys = []
    keypad = {(2,0):'D',(1,1):'A',(2,1):'B',(3,1):'C',(0,2):5,(1,2):6,(2,2):7,(3,2):8,(4,2):9,(1,3):2,(2,3):3,(3,3):4,(2,4):1}
    print(keypad)
    key = [0,2]
    for line in input:
        #print(line)
        for step in line:
            #print(step)
            if step == 'U' and (key[0],key[1]+1) in keypad:
                key=[key[0],key[1]+1]
            elif step == 'D' and (key[0],key[1]-1) in keypad:
                key=[key[0],key[1]-1]
            elif step == 'R' and (key[0]+1,key[1]) in keypad:
                key=[key[0]+1,key[1]]
            elif step == 'L' and (key[0]-1,key[1]) in keypad:
                key=[key[0]-1,key[1]]
            #else: print('No move')
            #print(step)
            #print(key,keypad[tuple(key)])

        #keys.append(list(keypad.keys())[list(keypad.values()).index(tuple(key))])
        keys.append(keypad[tuple(key)])
        print("*****")


    return keys
print(part2())
