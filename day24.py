#!/usr/bin/env python3
import numpy as np

with open('day24.txt') as f:
    data = f.read().split()
    data = [list(d) for d in data]
    data = np.array(data)
print(data)

def findstart(data):
    start = np.where(data == '0')
    return [int(start[0]),int(start[1]),0,['0']]

def iswall(data,nextm):
    return data[nextm[0]][nextm[1]] == '#'

def checknum(data,move):
    #are we located on a numeral? If yes, add it to state
    isnum = False
    c = data[move[0]][move[1]]
    if c in ['1','2','3','4','5','6','7','8','9'] and c not in move[3]:
        move[3] = move[3]+[c]
        return move
    else:
        return move
#print(checknum(data,[3, 1, 0, ['0']]))

#print(isnum(data,[3,1]))
def nextmoves(data,current):
    #print(current)
    moves = [[current[0]+1,current[1],current[2]+1,current[3]], [current[0]-1,current[1],current[2]+1,current[3]],[current[0],current[1]+1,current[2]+1,current[3]],[current[0],current[1]-1,current[2]+1,current[3]] ]
    return [ checknum(data,move) for move in moves  if not iswall(data,move[:2]) and move[0]>=0 and move[1]>=0 and move[:2] ]


def bfs(data,part):
    queue = [ findstart(data) ]
    
    #while loop
    #for i in range(10):
    while True:
        #print(queue)

        nextms = nextmoves(data,queue[0])
        if part == 1 and len([x for x in nextms if len(x[3]) == 5]) > 0:
            return [x for x in nextms if len(x[3]) == 5]
        queue = queue[1:]+nextms



print(bfs(data,1))
