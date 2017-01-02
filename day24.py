#!/usr/bin/env python3
import numpy as np

with open('day24.txt') as f:
    data = f.read().split()
    data = [list(d) for d in data]
    data = np.array(data)
# print(data)
# print(len(data),len(data[0]))

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
        #move[3].add(c)
        return move
    else:
        return move
#print(checknum(data,[3, 1, 0, set(['0','4'])]))

#print(isnum(data,[3,1]))
def nextmoves(data,current):
    #print(current)
    moves = [[current[0]+1,current[1],current[2]+1,current[3]], [current[0]-1,current[1],current[2]+1,current[3]],[current[0],current[1]+1,current[2]+1,current[3]],[current[0],current[1]-1,current[2]+1,current[3]] ]
    return [ checknum(data,move) for move in moves  if not iswall(data,move[:2]) ]


def bfs(data,part):

    queue = [ findstart(data) ]
    states = []
    n = 8
    i = 0
    #while loop
    #for i in range(10):
    while True:

        i += 1
        if i%1000 == 0:
            print(i,queue[0],len(queue))

        states = states + [queue[0][0:2]+[queue[0][3]]]
        nextms = [ x for x in nextmoves(data,queue[0]) if x[0:2]+[x[3]] not in states ]

        if part == 1 and len([x for x in nextms if len(x[3]) == n]) > 0:
            return [x for x in nextms if len(x[3]) == n]

        queue = queue[1:]+nextms
        #states = states + [set(x[3]) for x in nextms]



print(bfs(data,1))
