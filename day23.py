with open('day23.txt') as f:
    data = [x.strip().split() for x in f.readlines()]

d = {'a':12,'b':0,'c':0,'d':0}
i = 0
print(data)

def check(m):
    try:
        return int(m)
    except:
        return d[m]

while True:


    if  i >= len(data):
        print('****')
        break
    #print(data[i])
    if data[i][0] == 'cpy':
        d[data[i][2]] = check(data[i][1])

    elif data[i][0] == 'inc':
        d[data[i][1]] += 1

    elif data[i][0] == 'dec':
        d[data[i][1]] -= 1

    elif data[i][0] == 'jnz':
        if check(data[i][1]) != 0:
            i += check(data[i][2])
            i -= 1

    elif data[i][0] == 'tgl' and check(data[i][1])+i < len(data):
        newi = check(data[i][1])+i
        if data[newi][0] == 'inc':
            data[newi][0] = 'dec'
        elif data[newi][0] == 'dec' or data[newi][0] == 'tgl':
            data[newi][0] = 'inc'
        elif data[newi][0] == 'jnz':
            data[newi][0] = 'cpy'
        elif data[newi][0] == 'cpy':
            data[newi][0] = 'jnz'

    else: print('Bad input: {}, index {}, register {}'.format(data[i],i,d))
    #print(d,i)
    #print(data)
    i += 1


print(d)
