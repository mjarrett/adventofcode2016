#!/usr/bin/env python3
import random

data = 1358
#data = 10 #test
end = (31,39)
#end = [7,4] # test
queue = [[1,1,0]]
checked = {}
#check if a given tile is a wall
def iswall(nextm,data):
    x = nextm[0]
    y = nextm[1]
    loc = x*x + 3*x + 2*x*y + y + y*y + data
    loc = "{0:b}".format(loc)
    if loc.count('1')%2 == 0:
        return False
    else: return True

# check if there are any moves available
def nextmoves(current):
    moves = [[current[0]+1,current[1],current[2]+1],[current[0]-1,current[1],current[2]+1],[current[0],current[1]+1,current[2]+1],[current[0],current[1]-1,current[2]+1]]
    return [ move for move in moves if not iswall(move,data) and move[0] >= 0 and move[1] >= 0 and (move[0],move[1]) not in checked]

while len(queue) > 0:

    checked[(queue[0][0],queue[0][1])] = queue[0][2]
    queue = queue[1:] + [ move for move in nextmoves(queue[0]) if not ((move[0],move[1]) in checked) or (move[2] > checked[(move[0],move[1])])]
    #print(queue)
    #print(checked)
print(checked[end])
print(len([x for x in checked.values() if x < 51]) )
