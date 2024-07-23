basket, T = map(int, input().split())
blist = []

for i in range(1,basket+1):
    blist.append(0)

for n in range(1,T+1):
    i,j,k = map(int, input().split())

    for m in range(i-1,j):
        blist[m] = k

# *list하면 한줄 배열
print(*blist)