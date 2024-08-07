
a,b,v = map(int,input().split())
k = 0	#올라가는 데 걸리는 일수
'''
while 1:
    k+=1
    if a*k-b*(k-1)>=v:
        break
print(k)
'''

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)