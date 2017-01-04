with open('day25.txt') as f:
    data = [x.strip().split() for x in f.readlines()]



def check(m):
    try:
        return int(m)
    except:
        return d[m]

def run(d):
    i = 0
    result = []
    while True:

        #print(result)

        if  i >= len(data):
            break

        if data[i][0] == 'cpy':
            d[data[i][2]] = check(data[i][1])

        elif data[i][0] == 'inc':

            #check for cpy/inc/dec/jnz/dec/jnz loops:
            if data[i][1] in d:
                if (i>1 and i+4<len(data) and data[i-1][0] == 'cpy' and data[i+1][0] == 'dec'
                    and data[i+2][0] == 'jnz' and data[i+3][0] == 'dec' and data[i+4][0] == 'jnz'):

                    if data[i-1][2] == data[i+2][1] and data[i+1][1] == data[i-1][2] and data[i+3][1] == data[i+4][1] and data[i+2][2] == '-2' and data[i+4][2] == '-5':
                        d[data[i][1]] += check(data[i-1][2]) * check(data[i+3][1])
                        d[data[i+1][1]] = 0
                        d[data[i+3][1]] = 0
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
                elif data[newi][0] == 'dec' or data[newi][0] == 'tgl' or data[newi][0] == 'out':
                    data[newi][0] = 'inc'
                elif data[newi][0] == 'jnz':
                    data[newi][0] = 'cpy'
                elif data[newi][0] == 'cpy':
                    data[newi][0] = 'jnz'
            #else: print('toggle to outside range: {}, index {}, register {}'.format(data[i],i,d))

        elif data[i][0] == 'out':
            #print(check(data[i][1]))
            out = check(data[i][1])
            #print(result)
            #print(out)

            if (out == 1 or out == 0):
                result.append(check(data[i][1]))
            if len(result)>1 and out == result[-2]:
                return False

            if len(result) > 100:
                return True
        #else: print('Bad input: {}, index {}, register {}'.format(data[i],i,d))
        #print(d,i)
        #print(data)
        i += 1
    return d

k = 0
while True:
    d = {'a':k,'b':0,'c':0,'d':0}
    if run(d):
        print(k)
        break
    k += 1
