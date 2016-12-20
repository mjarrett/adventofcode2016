#!/usr/bin/env python3
import re
from hashlib import md5


def searchstring(myhash,k,givenc=False):

    for j,s in enumerate(myhash):
        if givenc == False:
            if j < len(myhash)-2 and myhash[j:j+k] == myhash[j]*k:
                return True,s
        else:
            if j < len(myhash)-2 and myhash[j:j+k] == givenc*k:
                return True,s
    return False,-1

def makehash(salt):
    mystr = 'ahsbgdzn'
    mystr = 'abc'
    m = md5()
    mystring = mystr + str(salt)
    m.update(mystring.encode('utf-8'))
    myhash = m.hexdigest()
    return myhash

def part1():
    i = 0

    triples = []
    numkeys = 0
    while True:

        myhash = makehash(i)
        is3,s = searchstring(myhash,3)
        if is3:
            for k in range(i+1,i+1001):
                myhash2 = makehash(k)
                is5,s2 = searchstring(myhash2,5,s)
                if is5:
                    numkeys = numkeys + 1
                    print(myhash,i,s,s2,k,numkeys)
                    if numkeys == 64:
                        return i


        i = i + 1

#print(part1())

def makehash2016(salt):
    myhash = makehash(salt)
    for i in range(2016):
        m = md5()
        m.update(myhash.encode('utf-8'))
        myhash = m.hexdigest()
    return myhash

def part2():
    i = 0

    triples = []
    numkeys = 0
    while True:

        myhash = makehash2016(i)
        is3,s = searchstring(myhash,3)
        if is3:
            for k in range(i+1,i+1001):
                myhash2 = makehash2016(k)
                is5,s2 = searchstring(myhash2,5,s)
                if is5:
                    numkeys = numkeys + 1
                    print(myhash,i,s,s2,k,numkeys)
                    if numkeys == 64:
                        return i


        i = i + 1

print(part2())
