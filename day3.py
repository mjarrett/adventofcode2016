#!/usr/bin/env python3

import pandas as pd

def part1():
    input = open('day3.txt')
    goods = []
    for line in input:
        sides = line.split()
        sides = list(map(int, sides))
        sides = sorted(sides)
        if sides[0]+sides[1] > sides[2]:
            goods.append(sides)
            #print(goods)

    print(len(goods))

def part2():
    input = open('day3.txt')
    df = pd.read_csv(input,header=None,names=[0,1,2],sep='\s+')
    count = 0
    goods = []
    for i in range(0,len(df),3):
        #print(i)
        d1 = [df.iloc[i][0],df.iloc[i+1][0],df.iloc[i+2][0]]
        d2 = [df.iloc[i][1],df.iloc[i+1][1],df.iloc[i+2][1]]
        d3 = [df.iloc[i][2],df.iloc[i+1][2],df.iloc[i+2][2]]

        d1 = sorted(list(map(int,d1)))
        d2 = sorted(list(map(int,d2)))
        d3 = sorted(list(map(int,d3)))

        for d in [d1, d2, d3]:
            if d[0] + d[1] > d[2]:
                goods.append(d)
    print(len(goods))

    #print(df)


part1()
part2()
