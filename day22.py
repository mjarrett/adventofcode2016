#!/usr/bin/env python3

with open('day22.txt') as f:
    data = f.read().strip().split('\n')
data = data[2:]
data = [x.split() for x in data]
data = [[x[0].replace('/dev/grid/node-x','')]+x[1:] for x in data]
data = [[x[0].replace('y',''),int(x[1].replace('T','')),int(x[2].replace('T','')),int(x[3].replace('T',''))] for x in data]
data = [[x[0].split('-')]+x[1:] for x in data]
data = [[(int(x[0][0]),int(x[0][1]))] + x[1:] for x in data]
ddata = {d[0]:d[1:] for d in data}

#print(ddata)

def part1(data):
    vpairs = []

    for a in ddata:
            for b in ddata:
                if a != b and ddata[a][1] > 0 and ddata[a][1] <= ddata[b][2]:
                    #print(a,ddata[a],b,ddata[b])
                    vpairs.append((a,b))
    return len(vpairs)

print('Part 1: {}'.format(part1(data)))

def part2(data):
    xmax = 36
    ymax = 26
    print(' ',*[' {}'.format(x) for x in range(10)]+[' {}'.format(x) for x in range(10)]+[' {}'.format(x) for x in range(10)]+[' {}'.format(x) for x in range(7)])
    for i in range(ymax+1):
        js = []
        for j in range(xmax+1):
            if ddata[(j,i)][1] > 100: js.append(' X ')
            elif (j,i) == (0,0): js.append('(.)')
            elif (j,i) == (xmax,0): js.append(' G ')
            elif ddata[(j,i)][1] == 0: js.append(' 0 ')
            else: js.append(' . ')
        #print(js)
        print(i,' ',*js, sep='')
part2(data)
print('Count the steps:\n- 33 steps to get (0,35) empty')
print('- 1 step to flip goal data and empty data')
print('- it now takes 5 steps to move goal data one step to the right')
print('- 34*5 steps to get the goal data to (0,1)')
print('- 4 steps to get (0,0) empty')
print('- 1 step to move goal data to (0,0)')
print('Part 2: {}'.format(33+1+34*5+5))
