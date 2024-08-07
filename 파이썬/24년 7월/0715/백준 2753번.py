
year = int(input()) # 연도 인풋 받기

flag = False #윤년 여부 확인 플래그

if year % 4 == 0:
    if year % 100 != 0 or year % 400 ==0:
        flag = True #윤년이면 True

else:
    flag = False


if flag == True:
    print("1")

else:
    print("0")