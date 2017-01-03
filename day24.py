#!/usr/bin/env python3
import numpy as np
import itertools as it

with open('day24.txt') as f:
    data = f.read().split()
    data = [list(d) for d in data]
    data = np.array(data)
# print(data)
# print(len(data),len(data[0]))

def findnum(data,N):
    start = np.where(data == N)
    return [int(start[0]),int(start[1])]

def iswall(data,nextm):
    return data[nextm[0]][nextm[1]] == '#'

def checknum(data,move,N):
    # are we at the number we're looking for?
    return N == data[move[0]][move[1]]

#print(isnum(data,[3,1]))
def nextmoves(data,current):
    #print(current)
    moves = [[current[0]+1,current[1],current[2]+1], [current[0]-1,current[1],current[2]+1],[current[0],current[1]+1,current[2]+1],[current[0],current[1]-1,current[2]+1] ]
    return [ move for move in moves  if not iswall(data,move[:2]) ]


def bfs(data,start,end):

    start = findnum(data,start)
    end = findnum(data,end)
    queue = [ start + [0]]
    states = []

    i = 0
    #while loop
    #for i in range(10):
    while True:


        states = states + [queue[0][0:2]]
        nextms = [ x for x in nextmoves(data,queue[0]) if x[0:2] not in states ]
        #nextms = nextmoves(data,queue[0])
        if queue[0][:2] == end:
            print(end)
            return queue[0]

        queue = queue[1:]+nextms
        #print(queue)
        states = states + [ x[0:2] for x in nextms]

def tsp(data,part):
    nums = ['0','1','2','3','4','5','6','7']
    pairs = it.combinations(nums,2)
    dists = {pair:bfs(data,*pair)[2] for pair in pairs}
    if part == 1:
        routes = [['0']+list(route) for route in it.permutations(nums[1:])]
    elif part == 2:
        routes = [['0']+list(route)+['0'] for route in it.permutations(nums[1:])]
    else: return '<part> must be 1 or 2'
    return min( [ sum([ dists[tuple(sorted([d,route[i+1]]))] for i,d in enumerate(route) if i < len(route)-1]) for route in routes])

#print(bfs(data,'0','1'))
print(tsp(data,2))
