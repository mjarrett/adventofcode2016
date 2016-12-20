#!/usr/bin/env python3

#data = '10000'
data = '11100010111110100'
#dsize = 20
dsize = 272

def filldisc(data,dsize):
    while len(data) < dsize:
        data2 = data[::-1]
        data2 = data2.replace('1','2').replace('0','1').replace('2','0')
        data = data + '0' + data2
    data = data[:dsize]
    return data


def checksum(data):
    i=0
    data2 = ''
    while i < len(data):
        #print(data[i:i+2])
        if data[i] == data[i+1]:
            data2 = data2 + '1'
        else:
            data2 = data2 + '0'
        #print(data2)
        i = i + 2
    if len(data2)%2 == 0:
        return checksum(data2)
    else:
        return data2


#data = filldisc(data)
#print(filldisc(data,dsize))
print(checksum(filldisc(data,dsize)))
print(checksum(filldisc(data,35651584)))
