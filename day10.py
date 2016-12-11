#!/usr/bin/env python3
import re

test1 = 61
test2 = 17
infile = 'day10.txt'
# test1 = 2
# test2 = 5

def solution(part):
    bots = {}
    instructs = {}
    output = {}

    with open(infile) as h:
        data = [ x.strip() for x in h.readlines()]


    for line in data:
        m1 = re.match('value (\d+) goes to bot (\d+)',line)
        if m1:
            bots.setdefault(m1.group(2),[]).append(int(m1.group(1))) # a trick to append if exists, create list if doesn't exist
    # print(bots)
    # print('*****')

    while True:
        for line in data:
            m2 = re.match('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)',line)
            if m2 and m2.group(1) in bots and  len(bots[m2.group(1)]) == 2:
                if part == 1 and ([test1,test2] == bots[m2.group(1)] or [test2,test1] == bots[m2.group(1)]): return m2.group(1)
                # print("return check: ")
                # print(bots[m2.group(1)])
                # print(line)
                if m2.group(2) == 'output':
                    output.setdefault(m2.group(3),[]).append(min(bots[m2.group(1)]))
                if m2.group(4) == 'output':
                    output.setdefault(m2.group(5),[]).append(max(bots[m2.group(1)]))
                if m2.group(2) == 'bot':
                    bots.setdefault(m2.group(3),[]).append(min(bots[m2.group(1)]))
                if m2.group(4) == 'bot':
                    bots.setdefault(m2.group(5),[]).append(max(bots[m2.group(1)]))
                bots[m2.group(1)] = []

            # print('bots: ')
            # print(bots)
            # print('outputs: ')
            # print(output)
            if  part == 2 and ('0' in output and '1' in output and '2' in output):
                print('Final: ')
                print(output['0'],output['1'],output['2'])
                return output['0'][0]*output['1'][0]*output['2'][0]


#cprint(solution(1))
print(solution(2))
