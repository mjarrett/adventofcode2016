#!/usr/bin/env python3
import pandas as pd

data = open('day6.txt')
rows = []
for line in data:
    rows.append(list(line.strip()))
df = pd.DataFrame(rows)

def part1():

    return ''.join(list(df.mode().iloc[0]))
#print(part1())

def part2():
    result = []
    for i in range(8):

        result.append(df[i].value_counts().idxmin())
    return ''.join(result)
print(part2())
