#!/usr/bin/env python3

with open('day12.txt') as f:
    data = [x.strip().split() for x in f.readlines()]

d = {'a':0,'b':0,'c':1,'d':0}
i = 0
print(data)

def check(m):
    try:
        return int(m)
    except:
        return d[m]

while True:
    # print(data[i])
    # print(d,i)
    if  i >= len(data): break
    if data[i][0] == 'cpy':
        d[data[i][2]] = check(data[i][1])

    elif data[i][0] == 'inc':
        d[data[i][1]] += 1

    elif data[i][0] == 'dec':
        d[data[i][1]] -= 1

    # elif data[i][0] == 'jnz':
    #     if check(data[i][1]) != 0:
    #         i += check(data[i][2])
    #         i += 1
    elif data[i][0] == 'jnz':
        if check(data[i][1]) != 0:
            i += check(data[i][2])
            i -= 1
    else: print('Bad input')
    i += 1


print(d)
