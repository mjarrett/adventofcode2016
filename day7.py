#!/usr/bin/env python3
import re


def find_abba(line):
    #print(line)
    abbas = []
    for i,c in enumerate(line):
        if i<len(line)-3 and line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
            abbas.append(line[i:i+4])
    return abbas

def part1():
    data = open('/Users/msj/github/adventofcode2016/day7.txt')
    tls_list = []
    for line in data:
        inabba = False
        outabba = False

        matches = re.findall('\[(\w+)\]',line)
        if matches:
            for match in matches:
                loc = line.find(match)
                line = line[:loc-1]+' '+line[loc+len(match)+1:] #leave space in
                if(len(find_abba(match))>0): inabba = True
        if(len(find_abba(line))>0): outabba = True
        if outabba and not inabba:
            tls_list.append(line)
    print(len(tls_list))

def find_aba(line):
    abas = []
    for i,c in enumerate(line):
        if i<len(line)-2 and line[i] == line[i+2] and line[i] != line[i+1]:
            abas.append(line[i:i+3])
    return abas

def part2():
    data = open('/Users/msj/github/adventofcode2016/day7.txt')

    ssl_list = []
    for line in data:
        isssl = False
        babs = []
        matches = re.findall('\[(\w+)\]',line)
        if matches:
            for match in matches:
                loc = line.find(match)
                line = line[:loc-1]+'  '+line[loc+len(match)+1:] 
                if(len(find_aba(match))>0):
                    babs.append(find_aba(match))
        babs = [item for sublist in babs for item in sublist]
        for bab in babs:
            if line.find(bab[1]+bab[0]+bab[1]) > -1: isssl = True
        if isssl: ssl_list.append(line)
    print(len(ssl_list))

part1()
part2()
