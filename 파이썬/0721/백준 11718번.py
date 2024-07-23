'''
while True:
    try:
        text = input()
        print(text)
        #EOFError는 더이상 문자를 읽을 수 없을 때 뜨는 에러임
        #input이 몇갠지 모르니까 예외가 에러인 상황
    except EOFError:
        break
'''
while True :
    try :
        print(input())
    except EOFError:
        break