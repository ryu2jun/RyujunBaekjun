

while True:
    N = int(input())
    result = ''
    ylist =[]
    if N == -1:
        break
    else:
        for n in range(1,N):
            if N % n == 0:     
                ylist.append(n)

            else:

                pass

        if N == sum(ylist):
            result += str(N)
            result += ' = '
            for i in range(0, len(ylist)):
                if i != len(ylist)-1:
                    result += str(ylist[i])
                    result += str(' + ')
                else:
                    result += str(ylist[i])

        else:
            result += str(N)
            result += ' is NOT perfect.'
        print(result)

    

'''
if N == sum(ylist):
    for i in range(0, len(ylist)-1):
        if i != len(ylist)-2:
            result += str(ylist[i])
            result += str(' + ')
        else:
            result += str(ylist[i])
    print(result)
else:
    print(str(N)+' is NOT perfect.')
'''