
test = []
for i in range(30):
    test.append(0)


for i in range(28):
    num = int(input())
    test[num-1] = 1

#번호가 28번 이상일 수 있으므로 30까지 검사해야 함
for i in range(30):
    if test[i] == 0:
        print(i+1)