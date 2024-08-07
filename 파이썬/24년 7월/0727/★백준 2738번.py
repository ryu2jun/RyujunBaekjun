N, M = map(int,input().split())

list1 = []
list2 = []



for i in range(N):
    put = list(map(int, input().split()))
    list1.append(put)

for i in range(N):
    put = list(map(int, input().split()))
    list2.append(put)

for i in range(0, N):
    for j in range(0, M):
        list1[i][j] += list2[i][j]
'''
        print(list1[i][j], end = ' ')
    print()
'''
for i in range(N):
    print(" ".join(map(str,list1[i])))
