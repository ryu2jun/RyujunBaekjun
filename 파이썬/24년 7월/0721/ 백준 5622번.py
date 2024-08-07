
d = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO':7, 'PQRS':8,'TUV':9,'WXYZ':10}

time = 0

text = input()
for i in range(0,len(text)):
    for j in d.keys():
        # 문자열의 요소가 문자열에 속해있는지 확인할 때 in을 쓸 수 있음
        if text[i] in j:
            time += d[j]
print(time)