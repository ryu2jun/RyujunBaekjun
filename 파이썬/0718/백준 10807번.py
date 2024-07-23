N = int(input())

#리스트로 입력받기

Nlist = list(map(int, input().split()))

compare = int(input())

result = 0
for i in Nlist:
    if i == compare:
        result += 1

print(result)