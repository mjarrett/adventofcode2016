#!/usr/bin/env python3
import random

data = 1358
end = (31,39)
checked = [] #spots that have been checked
current = (1,1)

def iswall(x,y):
    loc = x*x + 3*x + 2*x*y + y + y*y + data
    loc = "{0:b}".format(loc)
    if loc.count('1')%2 == 0:
        return False
    else: return True


def isvalid(state):
    x = state[0]
    y = state[1]
    if x < 0 or y < 0:
        return False
    elif (x,y) in checked:
        return False
    elif iswall(x,y):
        #print('wall')
        return False
    else: return True

def nextmove(current):
    #print('current {}'.format(current))
    xory = random.randint(0,1)
    forb = random.randint(0,1)*2-1
    nextm = list(current)
    nextm[xory] += forb
    #print('next {}'.format(nextm))
    if isvalid(nextm) == False:
        nextmove(current)
    return nextm


#walls (2,1),(1,0)
checked.append(current)
print(checked)
current = nextmove(current)
checked.append(current)
print(checked)
current = nextmove(current)
