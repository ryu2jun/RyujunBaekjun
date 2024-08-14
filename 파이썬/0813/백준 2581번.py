
N = int(input())
M = int(input())


result = []
for n in range(N, M+1):
    k = 1
    ylist = []
    while k < n:
        if n % k == 0:
            ylist.append(k)
        else:
            pass
        k += 1
    if len(ylist) == 1:
        result.append(n)

if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print("-1")

    

