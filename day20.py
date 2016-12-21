#!/usr/bin/env python3

nums = [x for x in range(4294967295+1)]
#print(nums)
with open('day20.txt') as f:
    for line in f:
        r = line.strip().split('-')
        amin = int(r[0])
        amax = int(r[1])+1
        #print(nums)
        #print(amin,amax)

        nums[amin:amax] = [-1]*(amax-amin)
    nums = [ x for x in nums if x > -1]
    print(min(nums))
