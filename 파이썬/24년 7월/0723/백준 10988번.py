
word = input()


result = []

if len(word) % 2 == 1:
    if len(word) == 1:
        result.append(True)
    else:
        for i in range(0, (len(word)-1)//2):
            if word[len(word)-1-i] == word[i]:
                result.append(1)
            else:
                result.append(0)



                
elif len(word) % 2 == 0:

    for i in range(0, len(word)//2):

        if word[i] == word[len(word)-1 - i]:
            result.append(1)
        else:
            result.append(0)




flag = True
for i in range(0, len(result)):

    if result[i] == 0:
        flag = False
        break

    else:
        flag = True

if flag == True:
    print("1")
else:
    print("0")

    