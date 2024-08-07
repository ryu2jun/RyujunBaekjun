
list1 = []

for i in range(9):
    put = list(map(int, input().split()))
    list1.append(put)

print(list1)

king = 0
I = 0
J = 0
for i in range(9):
    for j in range(9):
        if king <= list1[i][j]:
            king = list1[i][j]
            I = i+1
            J = j+1

print(king)
print(I, J)