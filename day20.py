#!/usr/bin/env python3

top = 9


with open('day20.txt') as f:
    data = [ x.split('-') for x in f.read().split()]
data = [ [int(x[0]),int(x[1])] for x in data ]
data = sorted(data)
#print(data)

count = 0

for i,d in enumerate(data):

    if count < d[0]:
        print(count)
        break
    print(count)
    count = d[1]+1
