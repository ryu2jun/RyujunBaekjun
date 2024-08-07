basket, T = map(int, input().split())
blist = []

for i in range(1,basket+1):
    blist.append(i)

for n in range(1,T+1):
    i,j = map(int, input().split())
    #요소간 지정으로 바꿀 수 있음
    blist[i-1], blist[j-1] = blist[j-1],blist[i-1]

# *list하면 한줄 배열
#end로도 한줄 배열 가능함
for i in range(basket):
    print(blist[i], end=' ')