
T = int(input())
mlist = [25, 10, 5, 1]

for i in range(T):
    change = int(input())
    clist = []
    for m in range(0,len(mlist)):

        clist.append(change//mlist[m])
        change %= mlist[m]
        change = round(change)

    print(*clist)