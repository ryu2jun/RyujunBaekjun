
list1 = []

for i in range(5):
    put = list(input())
    list1.append(put)


print(list1)


j = 0
for j in range(15):
    for i in range(0,5):
        if j < len(list1[i]):
            print(list1[i][j], end = '')
