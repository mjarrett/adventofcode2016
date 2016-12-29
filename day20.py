#!/usr/bin/env python3

top = 11
top = 4294967295
#top = 8327008

with open('day20.txt') as f:
    data = [ x.split('-') for x in f.read().split()]
data = [ [int(x[0]),int(x[1])] for x in data ]
data = sorted(data)
#print(data)

def part1(data):
    count = 0
    for i,d in enumerate(data):

        if count < d[0]:
            print(count)
            break
        count = d[1]+1

def part2(data):
    tip = 0
    result = 0
    #data = data[:100]
    for i,d in enumerate(data):
        #print(d,tip)
        if tip < d[0]:
            result += d[0]-tip
            #print(d,tip,result)

        if tip < d[1]:
            tip = d[1]+1
    if top > tip:
        result += top - tip
    print(result)
part1(data)
part2(data)
