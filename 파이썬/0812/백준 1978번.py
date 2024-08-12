
T = int(input())
N = list(map(int, input().split()))


result = 0
for n in N:
    k = 1
    ylist = []
    while k < n:
        if n % k == 0:
            ylist.append(k)
        else:
            pass
        k += 1
    if len(ylist) == 1:
        result += 1

print(result)

    

