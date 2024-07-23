hour, minuite = map(int, input().split())

if  hour > 0:
    if minuite >= 45:
        print(hour, minuite - 45)
    
    else:
        print(hour -1, 60 + minuite - 45)
        
elif hour == 0:
    if minuite >= 45:
        print(hour, minuite - 45)
    
    else:
        print(23, 60 + minuite - 45)