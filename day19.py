#!/usr/bin/env python3

from collections import deque
import numpy

data = 3014387
data = 5
#print(int(data/2)+1)

circle = deque([ [x,1] for x in range(1,data+1)])

#print(circle)

#for i in range(10):
while True:
    #print(circle[0],circle[1])
    if circle[0][1] == data:
        print(circle)
        break

    if circle[0][1] == 0:
        del circle[0]
    elif circle[0][1] > 0:
        circle[0][1] += circle[1][1]
        circle[1][1] = 0




    #print(len(circle))
    circle.rotate(-1)
    #print(i,circle)
