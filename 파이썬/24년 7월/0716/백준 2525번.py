hour, minuite = map(int, input().split())
ori = int(input())
'''
if hour < 23:
    if minuite + ori < 60:
        print(hour, minuite + ori)
    
    elif minuite + ori >= 60:
        if (minuite + ori) % 60 != 0:
            print(hour + (minuite + ori)//60, minuite + ori - 60)
        elif (minuite + ori) % 60 == 0:
            print(hour + (minuite + ori)//60, 0)

else:
    if minuite + ori < 60:
        print(0, minuite + ori)
    
    elif minuite + ori >= 60 and (minuite + ori) % 60 != 0:
        print(0 + (minuite + ori)//60 -1, minuite + ori - 60)
    
    elif minuite + ori >= 60 and (minuite + ori) % 60 == 0:
        print(0 + (minuite + ori)//60-1, 0)
'''

if minuite + ori < 60: #시간이 바뀌지 않는 경우
    print(hour, minuite + ori)

else: #시간이 바뀌는 경우
    if hour + (minuite + ori)//60 < 24: # 시간이 바뀌는 경우 중 24시 전인 경우
        if (minuite + ori) % 60 != 0: #시간이 딱 떨어지지 않는 경우
            print(hour + (minuite + ori)//60, minuite + ori - 60*((minuite + ori)//60))
    
        elif (minuite + ori) % 60 == 0: # 시간이 딱 떨어지는 경우
            print(hour + (minuite + ori)//60, 0)

    if hour + (minuite + ori)//60 >= 24: # 시간이 바뀌는 경우 중 24시 이후인 경우
        if (minuite + ori) % 60 != 0: #시간이 딱 떨어지지 않는 경우
            print(hour + (minuite + ori)//60 - 24, minuite + ori - 60*((minuite + ori)//60))
    
        elif (minuite + ori) % 60 == 0: # 시간이 딱 떨어지는 경우
            print(hour + (minuite + ori)//60 - 24, 0)

# 조리 시간이 500분 이렇게 60 이살일 수 도 있음을 계산 필요