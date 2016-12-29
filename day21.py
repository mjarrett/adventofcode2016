#!/usr/bin/env python3
from collections import deque
import random
s = 'abcdefgh'
#s = 'abcde'

with open('day21.txt') as f:
    data = f.read().strip().split('\n')
    data = [x.split() for x in data]

def rotate(s, n):
    l = list(s)
    l = l[-n:] + l[:-n]
    s = ''.join(l)
    return s

def doinst(s,d):
    #print(s,d)
    if d[0] == 'swap' and d[1] == 'letter':
        s = s.replace(d[2],'9')
        s = s.replace(d[5],d[2])
        s = s.replace('9',d[5])

    if d[0] == 'swap' and d[1] == 'position':
        p1 = int(d[2])
        p2 = int(d[5])
        c = sorted([[p1,s[p2]],[p2,s[p1]]])
        s = s[:c[0][0]] + c[0][1] + s[c[0][0]+1:c[1][0]] + c[1][1] + s[c[1][0]+1:]

    if d[0] == 'rotate' and d[1] == 'right':
        s = rotate(s,int(d[2]))
    if d[0] == 'rotate' and d[1] == 'left':
        s = rotate(s,-int(d[2]))
    if d[0] == 'rotate' and d[1] == 'based':
        p = s.find(d[-1])
        s = rotate(s,1+p)
        if p >= 4: s = rotate(s,1)

    if d[0] == 'reverse':
        s1 = s[int(d[2]):int(d[4])+1]
        s1 = s1[::-1]
        s = s[:int(d[2])]+s1+s[int(d[4])+1:]

    if d[0] == 'move':
        p1 = int(d[2])
        p2 = int(d[5])
        c1 = s[p1]
        s = s[:p1]+s[p1+1:]
        s = s[:p2]+c1+s[p2:]

    return s
# test = 'move position 3 to position 0'
# test = test.split()
# s = 'bdeac'
# print(doinst(s,test))
def scramble(data,s):
    for d in data:
        s = doinst(s,d)
        #print(s)
    return s
print('part 1: {}'.format(scramble(data,s)))

while True:
    s1 = ''.join(random.sample(s,len(s)))
    s2 = scramble(data,s1)
    #print(s1,s2)
    if s2 == 'fbgdceah':
        print('part 2: {}'.format(s1))
        break
