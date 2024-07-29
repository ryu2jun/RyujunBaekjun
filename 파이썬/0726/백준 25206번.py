
score = {'A+': 4.5,
         'A0': 4.0, 
         'B+': 3.5, 
         'B0': 3.0, 
         'C+': 2.5,
         'C0': 2.0,
         'D+': 1.5,
         'D0': 1.0, 
         'F': 0}
sumnum = 0
sumsco = 0
while True:
    words = input()
    if len(words) == 0:
        break
    else:
        words = list(words.split())
        sub = words[0]
        num = words[1]
        sco = words[2]
        
        if sco == 'P':
            pass

        else:
            sumnum += float(num)         
            sumsco += score[sco] * float(num)

    
    
print(round(sumsco/sumnum,6))

