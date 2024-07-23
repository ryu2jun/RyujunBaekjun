
chess = [1,1,2,2,2,8]

find =list(map(int, input().split()))


for i in range(0, len(find)):
    find[i] = chess[i] - find[i]

for i in find:
    print(i, end = ' ')