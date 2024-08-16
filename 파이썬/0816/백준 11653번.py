

N = int(input())
i = 2
while N!=1:
    if N%i == 0:
        print(i)
        N = N/i
    else:
        i+=1
'''
ylist = []
while N > 1:
    k = 2
    if N % k == 0:
        ylist.append(k)
        N /= k
    else:
        elselist = [] # 소인수 구할 리스트
        while len(elselist) < 1: #소인수 구하기
            k += 1
            n = 1
            nlist = [] #k가 소인수 인지 확인
            flag = False
            while n < k:
                if k % n == 0:
                    nlist.append(n)
                
                n += 1
            if len(nlist) == 1:
                flag = True
                if N % k == 0:
                    ylist.append(k)
                    elselist.append(k)

        N /= elselist[-1]

for i in ylist:
    print(i)
'''

