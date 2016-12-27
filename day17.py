#!/usr/bin/env python3
from hashlib import md5

# code = 'hijkl'
# code = 'ihgpwlah'
# code = 'kglvqrro'
# code = 'ulqzkmiv'
code = 'vkjiggvb'
queue = [[0,0,'']] #x, y, path so far
end = [3,3]
results = []

def makehash(base,salt):
    m = md5()
    mystring = base + salt
    m.update(mystring.encode('utf-8'))
    myhash = m.hexdigest()
    return myhash

def isopen(c):
    if c in 'bcdef':
        return True
    else: return False

def nextmoves(current):
    myhash = makehash(code,current[2])
    moves = [[current[0],current[1]-1,current[2]+'U'],[current[0],current[1]+1,current[2]+'D'],[current[0]-1,current[1],current[2]+'L'],[current[0]+1,current[1],current[2]+'R']]
    return [ move[0] for move in zip(moves,list(myhash[0:4])) if 4 > move[0][0] >=0 and 4 > move[0][1] >= 0 and isopen(move[1]) == True]

while len(queue) > 0:
    if [queue[0][0],queue[0][1]] == end:
        results.append(queue[0])
        queue = queue[1:]
    else:
        queue = queue[1:] + nextmoves(queue[0])

print(results[0][2])
print(len(results[-1][2]))
