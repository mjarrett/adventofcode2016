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
    print(i,data[i])

    if data[i][0] == 'cpy':
        d[data[i][2]] = check(data[i][1])

    elif data[i][0] == 'inc':

        #check for cpy/inc/dec/jnz/dec/jnz loops:
        if data[i][1] in d:
            if (i>1 and i+4<len(data) and data[i-1][0] == 'cpy' and data[i+1][0] == 'dec'
                and data[i+2][0] == 'jnz' and data[i+3][0] == 'dec' and data[i+4][0] == 'jnz'):

                if data[i-1][2] == data[i+2][1] and data[i+1][1] == data[i-1][2] and data[i+3][1] == data[i+4][1] and data[i+2][2] == '-2' and data[i+4][2] == '-5':
                    print('***')
                    print(data[i-1:i+4])
                    print(d)
                    d[data[i][1]] += check(data[i-1][2]) * check(data[i+3][1])
                    d[data[i+1][1]] = 0
                    d[data[i+3][1]] = 0
                    print(d)
                    i += 5
                    continue # goes back to start of while loop

        d[data[i][1]] += 1

    elif data[i][0] == 'dec':
        d[data[i][1]] -= 1

    elif data[i][0] == 'jnz':
        if check(data[i][1]) != 0:
            i += check(data[i][2])
            i -= 1

    elif data[i][0] == 'tgl':
        if check(data[i][1])+i < len(data):
            newi = check(data[i][1])+i
            if data[newi][0] == 'inc':
                data[newi][0] = 'dec'
            elif data[newi][0] == 'dec' or data[newi][0] == 'tgl':
                data[newi][0] = 'inc'
            elif data[newi][0] == 'jnz':
                data[newi][0] = 'cpy'
            elif data[newi][0] == 'cpy':
                data[newi][0] = 'jnz'
        else: print('toggle to outside range: {}, index {}, register {}'.format(data[i],i,d))



    else: print('Bad input: {}, index {}, register {}'.format(data[i],i,d))
    #print(d,i)
    #print(data)
    i += 1


print(d)
