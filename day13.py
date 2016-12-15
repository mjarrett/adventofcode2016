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



# check if a given move is valid
# def nextmove(current,checked):
#     #print('current {}'.format(current))
#     xory = random.randint(0,1)
#     forb = random.randint(0,1)*2-1
#     nextm = list(current)
#     nextm[xory] += forb
#     #print('next {}'.format(nextm))
#     if iswall(nextm)  or current[0] < 0 or current[1] < 0 or nextm in checked:
#         return nextmove(current,checked)
#     else: return nextm


# def one_path(current,allpaths):
#     checked = [] #spots that have been checked
#     while True:
#         #print(current)
#         #print(checked)
#         if current == end:
#             checked.append(current)
#             return True,len(checked)-1
#         if anymove(current,checked) == False:
#             #print('No moves from {}'.format(current))
#             #print('Path: {}'.format(checked))
#             checked.append(current)
#             return False,len(checked)-1
#
#         checked.append(current)
#         current = nextmove(current,checked)

def search(current):
    #print(current)
    # end conditions:
    if current == end:
        return True
    elif iswall(current):
        return False
    elif current in checked:
        return False
    elif current[0] < 0 or current[1] < 0:
        return False

    # if no end conditions met, current goes in checked
    checked.append(current)

    # explore neighbours recursively until and end condition is met. Respect walls
    # randomize search order
    xory = random.randint(0,1)
    forb = random.randint(0,1)*2-1
    next1 = list(current)
    next2 = list(current)
    next3 = list(current)
    next4 = list(current)
    next1[xory] = next1[xory]+forb
    next2[xory] = next2[xory]-forb
    next3[1-xory] = next3[1-xory]+forb
    next4[1-xory] = next4[1-xory]-forb
    if search(next1) or search(next2) or search(next3) or search(next4):
        return True
    return False

results = []
for i in range(10000):
    checked = []
    search([1,1])
    #print(checked)
    myset = set([tuple(x) for x in checked])
    results.append(len(myset))

print(min(results))





# while True:
#     allpaths = []
#     win,length = one_path(start,allpaths)
#
#     if win:
#         print(length)
