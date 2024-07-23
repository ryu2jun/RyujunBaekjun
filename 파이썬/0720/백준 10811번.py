basket, T = map(int, input().split())
blist = []

for i in range(1,basket+1):
    blist.append(i)

for n in range(T):
    i,j = map(int, input().split())
    blist2 =  blist[i-1:j]
    #리버스 함수를 써서 지정 부분의 역 리스트 저장
    blist2.reverse()

    #지정 부분과 역 리스트 부분을 교환
    blist[i-1:j] = blist2[:]

# *list하면 한줄 배열
#end로도 한줄 배열 가능함
for i in range(basket):
    print(blist[i], end=' ')