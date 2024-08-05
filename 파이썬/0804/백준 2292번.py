
N = int(input())
'''
count = 0
six = 1
while N>0:
    if N == 1:
        count += 1
        print(count)
        print(N)
        N -= 1
    else:
        N -= six * 6
        count += 1
        print(count)
        print(N)
        six+= 1

print(count)
'''
count = 0
six = 1
while N>0:
    if count == 0:
        N -= six
        count += 1
    else:
        six = count*6
        N -= six
        count += 1


print(count)