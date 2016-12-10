#!/usr/bin/env python3
import re
with open('day9.txt') as f:
    data = f.read().strip()
    #data = 'X(8x2)(3x3)ABCY'
    #data = '(6x1)(1x3)A'
    #data = 'A(2x2)BCD(2x2)EFG'

def part1(line):

        result = ""
        while len(line) > 0:
            #look for first instance of (AxB) in line
            m = re.search('\((\d+)x(\d+)\)',line)
            #if an (AxB) is found:
            # - add everything up to the start of (AxB) to result string
            # - add the repeating section to result string
            # - line now becomes everything from the end of the repeating section to the end of the string
            # Loop repeats and looks for first match in the new line
            if m:
                result = result + line[:m.start()] + line[m.end():m.end()+int(m.group(1))]*int(m.group(2))
                line =  line[m.end()+int(m.group(1)):]
                #print(len(result))

            # if not (AxB) is found:
            # - everything left in the line goes into the result string
            # - line is emptied to break the loop
            else:
                result = result + line
                line = ""
        print(len(result))

#part1(data)

def part11(line):


    result = 0
    m = re.search('\((\d+)x(\d+)\)',line)
    if not m:
        return result + len(line)

    #print(line[:m.start()],line[m.end():m.end()+int(m.group(1))]*int(m.group(2)),line[m.end()+int(m.group(1)):])
    return  len(line[:m.start()]) + len(line[m.end():m.end()+int(m.group(1))]*int(m.group(2))) + part11(line[m.end()+int(m.group(1)):])

#print(part11(data))

def part2(line):


    result = 0
    m = re.search('\((\d+)x(\d+)\)',line)
    if not m:
        return result + len(line)

    #print(line[:m.start()],line[m.end():m.end()+int(m.group(1))]*int(m.group(2)),line[m.end()+int(m.group(1)):])
    return  len(line[:m.start()]) + part2(line[m.end():m.end()+int(m.group(1))])*int(m.group(2)) + part2(line[m.end()+int(m.group(1)):])

print(part2(data))
