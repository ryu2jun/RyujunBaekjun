
N, B = input().split()

NUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(0, len(N)):
    for j in range(0,len(NUM)):
        if N[i] == NUM[j]:
            result += (j)*((int(B))**(len(N)-1-i))


print(result)