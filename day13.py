#!/usr/bin/env python3
import random

data = 1358
#data = 10 #test
end = [31,39]
#end = [7,4] # test
start = [1,1]

#check if a given tile is a wall
def iswall(nextm):
    x = nextm[0]
    y = nextm[1]
    loc = x*x + 3*x + 2*x*y + y + y*y + data
    loc = "{0:b}".format(loc)
    if loc.count('1')%2 == 0:
        return False
    else: return True


# check if a given move is valid
def nextmove(current,checked):
    #print('current {}'.format(current))
    xory = random.randint(0,1)
    forb = random.randint(0,1)*2-1
    nextm = list(current)
    nextm[xory] += forb
    #print('next {}'.format(nextm))
    if iswall(nextm)  or current[0] < 0 or current[1] < 0 or nextm in checked:
        return nextmove(current,checked)
    else: return nextm

# check if there are any moves available
def anymove(current,checked):
    moves = [[current[0]+1,current[1]],[current[0]-1,current[1]],[current[0],current[1]+1],[current[0],current[1]-1]]
    #print(moves)
    anygood = False
    for move in moves:
        #print(anygood)
        #print(move)
        if iswall(move)  or move[0] < 0 or move[1] < 0 or move in checked:
            anygood = False
        else: return True
    return anygood

#print(nextmove([1,1],[]))
#print(anymove([1,1],[[0,0],[0,1],[1,2]]))
def one_path(current,allpaths):
    checked = [] #spots that have been checked
    while True:
        #print(current)
        #print(checked)
        if current == end:
            checked.append(current)
            return True,len(checked)-1
        if anymove(current,checked) == False:
            #print('No moves from {}'.format(current))
            #print('Path: {}'.format(checked))
            checked.append(current)
            return False,len(checked)-1

        checked.append(current)
        current = nextmove(current,checked)


while True:
    allpaths = []
    win,length = one_path(start,allpaths)

    if win:
        print(length)
