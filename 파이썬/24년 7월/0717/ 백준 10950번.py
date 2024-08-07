

T = int(input())
result = []

for i in range(1, T+1):
    A, B = map(int, input().split( ))
    result.append(A+B)

for j in result:
    print(j)
# 저장해 놔야 하는 줄 알고 길게 코딩함..
'''
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)
'''