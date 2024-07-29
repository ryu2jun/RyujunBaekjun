

T= int(input())
result = 0

for i in range(T):
    word = input()
    group = []
    j = 0
    while j < len(word):

        if word[j] not in group:
            group.append(word[j])
        else:
            if word[j] == word[j-1]:
                group.append(word[j])
            else:
                break
        j += 1

    if len(word) == len(group):
        result += 1


    
    
print(result)