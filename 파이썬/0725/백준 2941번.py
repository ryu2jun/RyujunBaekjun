

word = input()

count = len(word)
for i in range(0, len(word)):

    if  word[i] == '=' and word[i-1] == 'z' and word[i-2] == 'd':
       count -= 2
    elif word[i] == '=':
        count -= 1
    
    elif word[i] == '-':
        count -= 1

    elif word[i]== 'j' and (word[i-1] == 'l' or word[i-1] == 'n'):
        count -= 1
        
print(count)

'''
replace()함수를 쓰면 간단하게 풀렸을 거임

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))

'''