N, K = map(int, input().split())
ylist =[]
n = 1

while n <= N:
    if N % n == 0:
        ylist.append(n)
    else:
        pass
    n += 1

if K <= len(ylist):
    print(ylist[K-1])
else:
    print("0")
