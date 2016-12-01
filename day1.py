#!/usr/bin/env python3

import numpy as np
import re

def part1():
    input = open('input.txt').read()

    input = input.split(',')

    n = 0 # x position (N/S)
    e = 0 # y position (E/W)
    f = 0 # facing (N=0, clockwise)
    for step in input:
        m = re.match('(\w)(\d+)',step.strip())
        turn = m.group(1)
        move = int(m.group(2))

        if turn == 'L': f = f - 1
        elif turn == 'R': f = f + 1
        else: print('Problem with input')

        if f%4 == 0: n = n + move
        elif f%4 == 2: n = n - move
        elif f%4 == 1: e = e + move
        elif f%4 == 3: e = e - move
        else: print('problem with processing')

        #print(turn,f%4,move,n,e)
    return abs(n)+abs(e)


def part2():
    input = open('input.txt').read()

    input = input.split(',')

    spots = [(0,0)]

    n = 0 #  position (N/S)
    e = 0 #  position (E/W)
    f = 0 # facing (N=0, clockwise)

    def check_spot(spots,spot):
        if spot in spots:
            return True
        else: return False
    for step in input:
        m = re.match('(\w)(\d+)',step.strip())
        turn = m.group(1)
        move = int(m.group(2))



        if turn == 'L': f = f - 1
        elif turn == 'R': f = f + 1
        else: print('Problem with input')

        #print(turn,f%4,move,e,n)

        if f%4 == 0:
            for i in range(1,move+1):
                spot = (e,n+i)
                if check_spot(spots,spot): return spot
                spots.append(spot)
            n = n + move
        elif f%4 == 2:
            for i in range(1,move+1):
                spot = (e,n-i)
                if check_spot(spots,spot): return spot
                spots.append(spot)
            n = n - move
        elif f%4 == 1:
            for i in range(1,move+1):
                spot = (e+i,n)
                if check_spot(spots,spot): return spot
                spots.append(spot)
            e = e + move
        elif f%4 == 3:
            for i in range(1,move+1):
                spot = (e-i,n)
                if check_spot(spots,spot): return spot
                spots.append(spot)
            e = e - move
        else: print('problem with processing')

        #print(spots)

    return "Didn't find a double spot!"
print(part1())
print(abs(part2()[0])+abs(part2()[1]))
