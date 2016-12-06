#!/usr/bin/env python3
import hashlib

data = 'reyedfim'
#data = 'abc'
def part1():
    results = []
    for i in range(10000000):
        m = hashlib.md5()
        mystring = data + str(i)
        m.update(mystring.encode('utf-8'))
        myhash = m.hexdigest()

        if myhash[:5] == '00000':
            print(myhash, i)
            results.append(myhash[5])
            if len(results) == 8:
                break
    return ''.join(results)

#print(part1())
def part2():
    results = [False]*8
    for i in range(1000000000):
    #for i in range(2):
        m = hashlib.md5()
        mystring = data + str(i)
        m.update(mystring.encode('utf-8'))
        myhash = m.hexdigest()
        if myhash[:5] == '00000' and myhash[5].isdigit():
            print(myhash,i)

            if int(myhash[5]) < 8 and results[int(myhash[5])] is False:
                #print(myhash, i)
                results[int(myhash[5])] = myhash[6]
                print(results)
                if False not in results:
                    print(results)
                    break
    return ''.join(results)

print(part2())
