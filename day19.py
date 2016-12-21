#!/usr/bin/env python3

from collections import deque

data = 3014387
#data = 5
#print(int(data/2)+1)

circle = deque([ [x,1] for x in range(1,data+1)])

def part1(circle,data):
    while True:
        #print(circle)
        if circle[0][1] == data:
            return circle

        if circle[0][1] > 0:
            circle[0][1] += circle[1][1]
            circle[1][1] = 0
            circle.rotate(-1)
        elif circle[0][1] == 0:
            del circle[0]

def part2(circle,data):
    while True:
        #print(circle)
        #if len(circle)%2 == 0:
        oppo = int(len(circle)/2)

        if circle[0][1] == data:
            return circle

        if circle[0][1] > 0:
            circle[0][1] += circle[oppo][1]
            circle[oppo][1] = 0
            circle.rotate(-1)
        elif circle[0][1] == 0:
            del circle[0]
print(part2(circle,data))
