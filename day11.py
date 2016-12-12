#!/usr/bin/env python3
import re

def init():
    with open('day11_test.txt') as f:
        data = [ x.strip() for x in f.readlines()]
    building = {}
    for line in data:
        floor = re.findall('The (\w+) floor',line)
        chips = re.findall('(\w+)-compatible',line)
        gens = re.findall('(\w+) generator',line)
        building[floor[0]] = {'chips':chips,'gens':gens}
    building[1] = building.pop('first')
    building[2] = building.pop('second')
    building[3] = building.pop('third')
    building[4] = building.pop('fourth')
    building['E'] = 1
    return building

building = init()
print(building)


****************
I ended up doing this one on pen and paper:
- Start by getting each generator/chip pair together
on one floor (X steps)
- Take one pair up to the top (Y steps)
- Then, each take a generator A down to bring
generator B up, then microchip A down, then
microchip B up, then generator A down, then
chip and generator A back up.
- Getting a pair up from the 3rd to 4th
floor takes 4 steps, plus 4 steps for each
additional floor
